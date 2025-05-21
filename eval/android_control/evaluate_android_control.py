
import numpy as np
import copy


BBOX_ENLARGE_FACTOR = 1.2
POINT_DISTANCE_THRESHOLD = 0.04

def check_text(text_pred, text_gt):
    text_pred = text_pred.lower().strip()
    text_gt = text_gt.lower().strip()
    return (text_pred in text_gt) or (text_gt in text_pred)


def check_click(click, candidate_bbox, gt_point, width, height):
    if len(candidate_bbox):
        candidate_bbox = enlarge_bbox(candidate_bbox, scale_factor=BBOX_ENLARGE_FACTOR)
        for bbox in candidate_bbox:
            if (bbox[0] <= click[0] <= bbox[2]) and (bbox[1] <= click[1] <= bbox[3]):
                return True
    if gt_point is not None:
        # Scale the distances by the respective dimensions to account for aspect ratio
        dx = (gt_point[0] - click[0]) * width
        dy = (gt_point[1] - click[1]) * height
        return np.sqrt(dx**2 + dy**2) <= POINT_DISTANCE_THRESHOLD * max(width, height)
    return False

def predict_direction(start, end):
    x1, y1 = start
    x2, y2 = end
    
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    if abs(delta_x) > abs(delta_y):
        if delta_x > 0:
            return 'right'
        else:
            return 'left'
    else:
        if delta_y > 0:
            return 'down'
        else:
            return 'up'

def enlarge_bbox(bbox_list, scale_factor=1.2)->np.ndarray:
 
    bbox_array = np.array(bbox_list)
    try:
        x_min, y_min, x_max, y_max = \
            bbox_array[:, 0], bbox_array[:, 1], bbox_array[:, 2], bbox_array[:, 3]
    except:
        print(bbox_array)
        raise
    
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    
    width = (x_max - x_min) * scale_factor
    height = (y_max - y_min) * scale_factor
    
    new_x_min = x_center - width / 2
    new_y_min = y_center - height / 2
    new_x_max = x_center + width / 2
    new_y_max = y_center + height / 2
    
    enlarged_bbox_list = np.vstack((new_x_min, new_y_min, new_x_max, new_y_max)).T
    
    return enlarged_bbox_list

def norm_coordinate(action, width, height):
    if 'candidate_bbox' in action:
        action['candidate_bbox'] = [[_[0]/width, _[1]/height, _[2]/width, _[3]/height] for _ in action['candidate_bbox']]
    if 'coordinate' in action:
        action['coordinate'] = [action['coordinate'][0]/width, action['coordinate'][1]/height]
    if 'coordinate2' in action:
        action['coordinate2'] = [action['coordinate2'][0]/width, action['coordinate2'][1]/height]
    return action

def evaluate_android_control_action(pred_action, current_check_pam, width, height, resized_width, resized_height, pred_type ='abs_resized', gt_type='original_resized'):
    pred_action = norm_coordinate(copy.deepcopy(pred_action), resized_width, resized_height) # todo use resized width
    current_check_pam = norm_coordinate(copy.deepcopy(current_check_pam), width, height)

    # type correct is ok
    if current_check_pam['action'] == 'wait':
        if pred_action['action'] == 'wait':
            return True, True
        return False, False
    elif current_check_pam['action'] == 'system_button':
        if pred_action['action'] == 'system_button':
            return True, current_check_pam['button'].lower().strip() == pred_action['button'].lower().strip()
        else:
            return False, False
    elif current_check_pam['action'] == 'type':
        if pred_action['action'] == 'type':
            return True, check_text(pred_action['text'], current_check_pam['text'])
        else:
            return False, False
    elif current_check_pam['action'] == 'open':
        if pred_action['action'] == 'open':
            return True, check_text(pred_action['text'], current_check_pam['text'])
        elif pred_action['action'] == 'click':
            if len(current_check_pam.get('candidate_bbox', []))>0:
                return True, check_click(pred_action['coordinate'], current_check_pam['candidate_bbox'], gt_point=[(current_check_pam['candidate_bbox'][0][0]+current_check_pam['candidate_bbox'][0][2])/2, (current_check_pam['candidate_bbox'][0][1]+current_check_pam['candidate_bbox'][0][3])/2], width=resized_width, height=resized_height)
            else:
                return False, False
        else:
            return False, False
    elif current_check_pam['action'] == 'swipe':
        if pred_action['action'] == 'swipe':
            direction = predict_direction(pred_action['coordinate'], pred_action['coordinate2'])
            return True, direction == current_check_pam['direction']
        else:
            return False, False
    elif current_check_pam['action'] in ['long_press', 'click']:
        if pred_action['action'] == current_check_pam['action']:
            return True, check_click(pred_action['coordinate'], current_check_pam['candidate_bbox'], gt_point=current_check_pam['coordinate'], width=resized_width, height=resized_height)
        else:
            return False, False
    raise NotImplementedError

def makeup_android_control_message(action):
    if action['action'] == 'wait':
        return f"Current step query: Wait for {action['time']} seconds\nTask progress (You have done the following operation on the current device):"
    elif action['action'] == 'system_button':
        return f"Current step query: Press {action['button']} button\nTask progress (You have done the following operation on the current device):"
    else:
        return f"Current step query: {action['action']} {action['text']}\nTask progress (You have done the following operation on the current device):"