<h1 align="center">
<img src="images/InfiGUI-R1_logo.png" width="100" alt="InfiGUI-R1" />
<br>
InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners
</h1>

<p align="center">
  <a href="https://arxiv.org/abs/2504.14239"><img src="https://img.shields.io/badge/arXiv-Paper-b31b1b?style=flat&logo=arxiv&logoColor=white" alt="arXiv Paper"></a>
  <a href="https://huggingface.co/papers/2504.14239"><img src="https://img.shields.io/badge/🤗%20HuggingFace-Daily%20Papers-ff9800?style=flat" alt="Hugging Face Paper"></a>
  <a href="https://huggingface.co/Reallm-Labs/InfiGUI-R1-3B"><img src="https://img.shields.io/badge/🤗%20HuggingFace-Models-ff9800?style=flat" alt="Hugging Face Model"></a>
</p>

<br>
<p align="center">
  <strong>This is the official repository for the paper <a href="https://arxiv.org/abs/2504.14239">InfiGUI-R1</a>.</strong>
</p>

## 🌟 Overview

In this work, we develop **InfiGUI-R1**, a multimodal large language model-based GUI agent primarily trained using **Reinforcement Learning** to enhance planning and error recovery skills for GUI tasks. Specifically, our agent is trained using a two-stage framework: first, we inject spatial reasoning capabilities by distilling reasoning trajectories from teacher models; second, we enhance the agent's planning and error recovery skills using Reinforcement Learning, employing techniques like rewarding accurate sub-goal generation and training on constructed error recovery scenarios.

<div align="center">
  <img src="images/method.png" width="70%" alt="Method Overview">
  <p><i>Our two-stage training framework</i></p>
</div>

<div align="center">
  <img src="images/screenspot-pro.png" width="70%" alt="Results on ScreenSpot Pro">
  <p><i>Performance results on ScreenSpot Pro benchmark</i></p>
</div>

## 🔥 News

- 🔥 ***`2025/4/19`*** Our paper "[InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239)" released.
- 🔥 ***`2025/1/9`*** Our paper "[InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection](https://arxiv.org/abs/2501.04575)" released.
- 🔥 ***`2024/12/12`*** Our paper "[OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://os-agent-survey.github.io/)" released.
- ***`2024/4/2`*** Our paper "[InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks](https://infiagent.github.io/)" is accepted by *ICML 2024*.

## 🚀 Updates

- ***`2025/04/20`*** [Model weights](https://huggingface.co/Reallm-Labs/InfiGUI-R1-3B) have been uploaded to Hugging Face.
- ***`2025/04/19`*** [Our preprint](https://arxiv.org/abs/2504.14239) has been published on arXiv.

## 📊 Results

### ScreenSpot Results

On the cross-platform [ScreenSpot](https://github.com/njucckevin/SeeClick) benchmark, InfiGUI-R1-3B achieves an average accuracy of **87.5%**. It leads across text and icon localization tasks on Mobile, Desktop, and Web platforms, reaching the state-of-the-art level for models of similar parameter size (as of 2025/04/19):

<div align="center">
<table border="1">
  <thead>
    <tr><th rowspan="2" align="left">Model</th><th colspan="2" align="center">Mobile</th><th colspan="2" align="center">Desktop</th><th colspan="2" align="center">Web</th><th rowspan="2" align="center">Avg.</th></tr>
    <tr><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th></tr>
  </thead>
  <tbody>
    <tr><th colspan="8" align="left"><em>Proprietary Models</em></th></tr>
    <tr><td align="left">GPT-4o</td><td align="center">30.5</td><td align="center">23.2</td><td align="center">20.6</td><td align="center">19.4</td><td align="center">11.1</td><td align="center">7.8</td><td align="center">18.8</td></tr>
    <tr><td align="left">Claude Computer Use</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">83.0</td></tr>
    <tr><td align="left">Gemini 2.0 (Project Mariner)</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">84.0</td></tr>
    <tr><th colspan="8" align="left"><em>General Open-source Models</em></th></tr>
    <tr><td align="left">Qwen2-VL-7B</td><td align="center">61.3</td><td align="center">39.3</td><td align="center">52.0</td><td align="center">45.0</td><td align="center">33.0</td><td align="center">21.8</td><td align="center">42.9</td></tr>
    <tr><td align="left">Qwen2.5-VL-3B</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">55.5</td></tr>
    <tr><td align="left">Qwen2.5-VL-7B</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center"><ins>84.7</ins></td></tr>
    <tr><th colspan="8" align="left"><em>GUI-specific Models</em></th></tr>
    <tr><td align="left">CogAgent</td><td align="center">67.0</td><td align="center">24.0</td><td align="center">74.2</td><td align="center">20.0</td><td align="center">70.4</td><td align="center">28.6</td><td align="center">47.4</td></tr>
    <tr><td align="left">SeeClick</td><td align="center">78.0</td><td align="center">52.0</td><td align="center">72.2</td><td align="center">30.0</td><td align="center">55.7</td><td align="center">32.5</td><td align="center">53.4</td></tr>
    <tr><td align="left">UGround-7B</td><td align="center">82.8</td><td align="center">60.3</td><td align="center">82.5</td><td align="center">63.6</td><td align="center">80.4</td><td align="center">70.4</td><td align="center">73.3</td></tr>
    <tr><td align="left">OS-Atlas-7B</td><td align="center">93.0</td><td align="center">72.9</td><td align="center">91.8</td><td align="center">62.9</td><td align="center">90.9</td><td align="center">74.3</td><td align="center">82.5</td></tr>
    <tr><td align="left">ShowUI-2B</td><td align="center">92.3</td><td align="center">75.5</td><td align="center">76.3</td><td align="center">61.1</td><td align="center">81.7</td><td align="center">63.6</td><td align="center">75.1</td></tr>
    <tr><td align="left">Aguvis-7B</td><td align="center"><ins>95.6</ins></td><td align="center">77.7</td><td align="center"><ins>93.8</ins></td><td align="center">67.1</td><td align="center">88.3</td><td align="center">75.2</td><td align="center">84.4</td></tr>
    <tr><td align="left">UI-R1-3B</td><td align="center">-</td><td align="center">-</td><td align="center">90.2</td><td align="center">59.3</td><td align="center">85.2</td><td align="center">73.3</td><td align="center">-</td></tr>
    <tr><td align="left">GUI-R1-3B</td><td align="center">-</td><td align="center">-</td><td align="center"><ins>93.8</ins></td><td align="center">64.8</td><td align="center">89.6</td><td align="center">72.1</td><td align="center">-</td></tr>
    <tr><td align="left">GUI-R1-7B</td><td align="center">-</td><td align="center">-</td><td align="center">91.8</td><td align="center"><ins>73.6</ins></td><td align="center"><ins>91.3</ins></td><td align="center"><ins>75.7</ins></td><td align="center">-</td></tr>
    <tr><td align="left">UI-TARS-2B</td><td align="center">93.0</td><td align="center">75.5</td><td align="center">90.7</td><td align="center">68.6</td><td align="center">84.3</td><td align="center">74.8</td><td align="center">82.3</td></tr>
    <tr><th colspan="8" align="left"><em>Ours</em></th></tr>
    <tr><td align="left"><b>InfiGUI-R1-3B</b></td><td align="center"><b>97.1</b></td><td align="center"><b>81.2</b></td><td align="center"><b>94.3</b></td><td align="center"><b>77.1</b></td><td align="center"><b>91.7</b></td><td align="center"><b>77.6</b></td><td align="center"><b>87.5</b></td></tr>
  </tbody>
</table>
</div>

### ScreenSpot-Pro Results

On the more challenging [ScreenSpot-Pro](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) benchmark, which focuses on complex high-resolution desktop applications, InfiGUI-R1-3B achieves an average accuracy of **35.7%**. This performance rivals that of larger 7B models with excellent performance, reaching the state-of-the-art level for models of similar parameter size (as of 2025/04/19).

<div align="center">
<table border="1">
  <thead>
    <tr><th rowspan="3" align="left">Model&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th><th colspan="3" align="center">Avg.</th><th colspan="3" align="center">CAD</th><th colspan="3" align="center">Development</th><th colspan="3" align="center">Creative</th><th colspan="3" align="center">Scientific</th><th colspan="3" align="center">Office</th><th colspan="3" align="center">OS</th></tr>
    <tr><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th><th colspan="2" align="center">Acc</th><th rowspan="2" align="center">Avg.</th></tr>
    <tr><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th><th align="center">Text</th><th align="center">Icon</th></tr>
  </thead>
  <tbody>
    <tr><th colspan="22" align="left"><em>Proprietary Models</em></th></tr>
    <tr><td align="left">GPT-4o</td><td align="center">1.3</td><td align="center">0.0</td><td align="center">0.8</td><td align="center">2.0</td><td align="center">0.0</td><td align="center">1.5</td><td align="center">1.3</td><td align="center">0.0</td><td align="center">0.7</td><td align="center">1.0</td><td align="center">0.0</td><td align="center">0.6</td><td align="center">2.1</td><td align="center">0.0</td><td align="center">1.2</td><td align="center">1.1</td><td align="center">0.0</td><td align="center">0.9</td><td align="center">0.0</td><td align="center">0.0</td><td align="center">0.0</td></tr>
    <tr><td align="left">Claude Computer Use</td><td align="center">23.4</td><td align="center">7.1</td><td align="center">17.1</td><td align="center">14.5</td><td align="center">3.7</td><td align="center">11.9</td><td align="center">22.0</td><td align="center">3.9</td><td align="center">12.6</td><td align="center">25.9</td><td align="center">3.4</td><td align="center">16.8</td><td align="center">33.9</td><td align="center">15.8</td><td align="center">25.8</td><td align="center">30.1</td><td align="center">16.3</td><td align="center">26.9</td><td align="center">11.0</td><td align="center">4.5</td><td align="center">8.1</td></tr>
    <tr><th colspan="22" align="left"><em>General Open-source Models</em></th></tr>
    <tr><td align="left">Qwen2-VL-7B</td><td align="center">2.5</td><td align="center">0.2</td><td align="center">1.6</td><td align="center">0.5</td><td align="center">0.0</td><td align="center">0.4</td><td align="center">2.6</td><td align="center">0.0</td><td align="center">1.3</td><td align="center">1.5</td><td align="center">0.0</td><td align="center">0.9</td><td align="center">6.3</td><td align="center">0.0</td><td align="center">3.5</td><td align="center">3.4</td><td align="center">1.9</td><td align="center">3.0</td><td align="center">0.9</td><td align="center">0.0</td><td align="center">0.5</td></tr>
    <tr><td align="left">Qwen2.5-VL-3B</td><td align="center">-</td><td align="center">-</td><td align="center">23.9</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
    <tr><td align="left">Qwen2.5-VL-7B</td><td align="center">-</td><td align="center">-</td><td align="center">29.0</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
    <tr><td align="left">Kimi-VL</td><td align="center">-</td><td align="center">-</td><td align="center"><ins>34.5</ins></td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
    <tr><th colspan="22" align="left"><em>GUI-specific Models</em></th></tr>
    <tr><td align="left">SeeClick</td><td align="center">1.8</td><td align="center">0.0</td><td align="center">1.1</td><td align="center">2.5</td><td align="center">0.0</td><td align="center">1.9</td><td align="center">0.6</td><td align="center">0.0</td><td align="center">0.3</td><td align="center">1.0</td><td align="center">0.0</td><td align="center">0.6</td><td align="center">3.5</td><td align="center">0.0</td><td align="center">2.0</td><td align="center">1.1</td><td align="center">0.0</td><td align="center">0.9</td><td align="center">2.8</td><td align="center">0.0</td><td align="center">1.5</td></tr>
    <tr><td align="left">CogAgent-18B</td><td align="center">12.0</td><td align="center">0.8</td><td align="center">7.7</td><td align="center">7.1</td><td align="center">3.1</td><td align="center">6.1</td><td align="center">14.9</td><td align="center">0.7</td><td align="center">8.0</td><td align="center">9.6</td><td align="center">0.0</td><td align="center">5.6</td><td align="center">22.2</td><td align="center">1.8</td><td align="center">13.4</td><td align="center">13.0</td><td align="center">0.0</td><td align="center">10.0</td><td align="center">5.6</td><td align="center">0.0</td><td align="center">3.1</td></tr>
    <tr><td align="left">Aria-UI</td><td align="center">17.1</td><td align="center">2.0</td><td align="center">11.3</td><td align="center">7.6</td><td align="center">1.6</td><td align="center">6.1</td><td align="center">16.2</td><td align="center">0.0</td><td align="center">8.4</td><td align="center">23.7</td><td align="center">2.1</td><td align="center">14.7</td><td align="center">27.1</td><td align="center">6.4</td><td align="center">18.1</td><td align="center">20.3</td><td align="center">1.9</td><td align="center">16.1</td><td align="center">4.7</td><td align="center">0.0</td><td align="center">2.6</td></tr>
    <tr><td align="left">OS-Atlas-4B</td><td align="center">5.0</td><td align="center">1.7</td><td align="center">3.7</td><td align="center">2.0</td><td align="center">0.0</td><td align="center">1.5</td><td align="center">7.1</td><td align="center">0.0</td><td align="center">3.7</td><td align="center">3.0</td><td align="center">1.4</td><td align="center">2.3</td><td align="center">9.0</td><td align="center">5.5</td><td align="center">7.5</td><td align="center">5.1</td><td align="center">3.8</td><td align="center">4.8</td><td align="center">5.6</td><td align="center">0.0</td><td align="center">3.1</td></tr>
    <tr><td align="left">OS-Atlas-7B</td><td align="center">28.1</td><td align="center">4.0</td><td align="center">18.9</td><td align="center">12.2</td><td align="center">4.7</td><td align="center">10.3</td><td align="center">33.1</td><td align="center">1.4</td><td align="center">17.7</td><td align="center">28.8</td><td align="center">2.8</td><td align="center">17.9</td><td align="center">37.5</td><td align="center">7.3</td><td align="center">24.4</td><td align="center">33.9</td><td align="center">5.7</td><td align="center">27.4</td><td align="center">27.1</td><td align="center">4.5</td><td align="center">16.8</td></tr>
    <tr><td align="left">ShowUI-2B</td><td align="center">10.8</td><td align="center">2.6</td><td align="center">7.7</td><td align="center">2.5</td><td align="center">0.0</td><td align="center">1.9</td><td align="center">16.9</td><td align="center">1.4</td><td align="center">9.4</td><td align="center">9.1</td><td align="center">0.0</td><td align="center">5.3</td><td align="center">13.2</td><td align="center">7.3</td><td align="center">10.6</td><td align="center">15.3</td><td align="center">7.5</td><td align="center">13.5</td><td align="center">10.3</td><td align="center">2.2</td><td align="center">6.6</td></tr>
    <tr><td align="left">UGround-7B</td><td align="center">25.0</td><td align="center">2.8</td><td align="center">16.5</td><td align="center">14.2</td><td align="center">1.6</td><td align="center">11.1</td><td align="center">26.6</td><td align="center">2.1</td><td align="center">14.7</td><td align="center">27.3</td><td align="center">2.8</td><td align="center">17.0</td><td align="center">31.9</td><td align="center">2.7</td><td align="center">19.3</td><td align="center">31.6</td><td align="center">11.3</td><td align="center">27.0</td><td align="center">17.8</td><td align="center">0.0</td><td align="center">9.7</td></tr>
    <tr><td align="left">UGround-V1-7B</td><td align="center">-</td><td align="center">-</td><td align="center">31.1</td><td align="center">-</td><td align="center">-</td><td align="center">13.5</td><td align="center">-</td><td align="center">-</td><td align="center"><ins>35.5</ins></td><td align="center">-</td><td align="center">-</td><td align="center">27.8</td><td align="center">-</td><td align="center">-</td><td align="center">38.8</td><td align="center">-</td><td align="center">-</td><td align="center">48.8</td><td align="center">-</td><td align="center">-</td><td align="center"><ins>26.1</ins></td></tr>
    <tr><td align="left">UI-R1-3B</td><td align="center">-</td><td align="center">-</td><td align="center">17.8</td><td align="center">11.2</td><td align="center">6.3</td><td align="center">-</td><td align="center">22.7</td><td align="center">4.1</td><td align="center">-</td><td align="center">27.3</td><td align="center">3.5</td><td align="center">-</td><td align="center">42.4</td><td align="center">11.8</td><td align="center">-</td><td align="center">32.2</td><td align="center">11.3</td><td align="center">-</td><td align="center">13.1</td><td align="center">4.5</td><td align="center">-</td></tr>
    <tr><td align="left">GUI-R1-3B</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center"><ins>26.4</ins></td><td align="center">7.8</td><td align="center">-</td><td align="center">33.8</td><td align="center"><ins>4.8</ins></td><td align="center">-</td><td align="center">40.9</td><td align="center">5.6</td><td align="center">-</td><td align="center"><ins>61.8</ins></td><td align="center">17.3</td><td align="center">-</td><td align="center">53.6</td><td align="center">17.0</td><td align="center">-</td><td align="center">28.1</td><td align="center">5.6</td><td align="center">-</td></tr>
    <tr><td align="left">GUI-R1-7B</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">23.9</td><td align="center">6.3</td><td align="center">-</td><td align="center">49.4</td><td align="center"><ins>4.8</ins></td><td align="center">-</td><td align="center">38.9</td><td align="center"><ins>8.4</ins></td><td align="center">-</td><td align="center">55.6</td><td align="center">11.8</td><td align="center">-</td><td align="center">58.7</td><td align="center"><ins>26.4</ins></td><td align="center">-</td><td align="center"><ins>42.1</ins></td><td align="center"><b>16.9</b></td><td align="center">-</td></tr>
    <tr><td align="left">UI-TARS-2B</td><td align="center">39.6</td><td align="center">8.4</td><td align="center">27.7</td><td align="center">17.8</td><td align="center">4.7</td><td align="center">14.6</td><td align="center">47.4</td><td align="center">4.1</td><td align="center">26.4</td><td align="center">42.9</td><td align="center">6.3</td><td align="center">27.6</td><td align="center">56.9</td><td align="center">17.3</td><td align="center">39.8</td><td align="center">50.3</td><td align="center">17.0</td><td align="center">42.6</td><td align="center">21.5</td><td align="center">5.6</td><td align="center">14.3</td></tr>
    <tr><td align="left">UI-TARS-7B</td><td align="center"><ins>47.8</ins></td><td align="center"><b>16.2</b></td><td align="center"><b>35.7</b></td><td align="center">20.8</td><td align="center"><ins>9.4</ins></td><td align="center"><ins>18.0</ins></td><td align="center"><b>58.4</b></td><td align="center"><b>12.4</b></td><td align="center"><b>36.1</b></td><td align="center"><b>50.0</b></td><td align="center"><b>9.1</b></td><td align="center"><b>32.8</b></td><td align="center"><b>63.9</b></td><td align="center"><b>31.8</b></td><td align="center"><b>50.0</b></td><td align="center"><ins>63.3</ins></td><td align="center">20.8</td><td align="center"><ins>53.5</ins></td><td align="center">30.8</td><td align="center"><b>16.9</b></td><td align="center">24.5</td></tr>
    <tr><th colspan="22" align="left"><em>Ours</em></th></tr>
    <tr><td align="left"><b>InfiGUI-R1-3B</b></td><td align="center"><b>49.1</b></td><td align="center"><ins>14.1</ins></td><td align="center"><b>35.7</b></td><td align="center"><b>33.0</b></td><td align="center"><b>14.1</b></td><td align="center"><b>28.4</b></td><td align="center"><ins>51.3</ins></td><td align="center"><b>12.4</b></td><td align="center">32.4</td><td align="center"><ins>44.9</ins></td><td align="center">7.0</td><td align="center"><ins>29.0</ins></td><td align="center">58.3</td><td align="center"><ins>20.0</ins></td><td align="center"><ins>41.7</ins></td><td align="center"><b>65.5</b></td><td align="center"><b>28.3</b></td><td align="center"><b>57.0</b></td><td align="center"><b>43.9</b></td><td align="center"><ins>12.4</ins></td><td align="center"><b>29.6</b></td></tr>
  </tbody>
</table>
</div>

### AndroidControl Results

On the [AndroidControl](https://github.com/google-research/google-research/tree/master/android_control), which involves diverse Android trajectory tasks (with Low and High difficulty levels), InfiGUI-R1-3B achieves success rates on its test split of **92.1%** and **71.1%**, respectively. This reaches the state-of-the-art level for models of similar parameter size (as of 2025/04/19).

<div align="center">
<table border="1">
  <thead>
    <tr><th rowspan="2" align="left">Model</th><th colspan="3" align="center">AndroidControl-Low</th><th colspan="3" align="center">AndroidControl-High</th></tr>
    <tr><th align="center">Type</th><th align="center">Grounding</th><th align="center">SR</th><th align="center">Type</th><th align="center">Grounding</th><th align="center">SR</th></tr>
  </thead>
  <tbody>
    <tr><td align="left">GPT-4o</td><td align="center">74.3</td><td align="center">0.0</td><td align="center">19.4</td><td align="center">66.3</td><td align="center">0.0</td><td align="center">20.8</td></tr>
    <tr><td align="left">Aria-UI</td><td align="center">–</td><td align="center"><ins>87.7</ins></td><td align="center">67.3</td><td align="center">–</td><td align="center">43.2</td><td align="center">10.2</td></tr>
    <tr><td align="left">OS-Atlas-4B</td><td align="center">91.9</td><td align="center">83.8</td><td align="center">80.6</td><td align="center"><b>84.7</b></td><td align="center">73.8</td><td align="center">67.5</td></tr>
    <tr><td align="left">Aguvis-7B</td><td align="center">–</td><td align="center">–</td><td align="center">80.5</td><td align="center">–</td><td align="center">–</td><td align="center">61.5</td></tr>
    <tr><td align="left">Aguvis-72B</td><td align="center">–</td><td align="center">–</td><td align="center">84.4</td><td align="center">–</td><td align="center">–</td><td align="center">66.4</td></tr>
    <tr><td align="left">UI-R1</td><td align="center">94.3</td><td align="center">82.6</td><td align="center">88.5</td><td align="center">-</td><td align="center">-</td><td align="center">-</td></tr>
    <tr><td align="left">GUI-R1-3B</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">58.0</td><td align="center">56.2</td><td align="center">46.6</td></tr>
    <tr><td align="left">GUI-R1-7B</td><td align="center">-</td><td align="center">-</td><td align="center">-</td><td align="center">71.6</td><td align="center">65.6</td><td align="center">51.7</td></tr>
    <tr><td align="left">UI-TARS-2B</td><td align="center"><b>98.1</b></td><td align="center">87.3</td><td align="center"><ins>89.3</ins></td><td align="center">81.2</td><td align="center"><b>78.4</b></td><td align="center"><ins>68.9</ins></td></tr>
    <tr><th colspan="7" align="left"><em>Ours</em></th></tr>
    <tr><td align="left"><b>InfiGUI-R1-3B</b></td><td align="center"><ins>96.0</ins></td><td align="center"><b>93.2</b></td><td align="center"><b>92.1</b></td><td align="center"><ins>82.7</ins></td><td align="center"><ins>74.4</ins></td><td align="center"><b>71.1</b></td></tr>
  </tbody>
</table>
</div>

## 🧪 Evaluation

### AndroidControl

To reproduce the results on AndroidControl:

1.  Install the `vllm` library:
    ```bash
    pip install vllm
    ```
2.  Navigate to the evaluation directory ([`eval/android_control`](https://github.com/Reallm-Labs/InfiGUI-R1/tree/main/eval/android_control)):
    ```bash
    cd eval/android_control
    ```
3.  Download the processed test set from Hugging Face ([`Reallm-Labs/android_control_test`](https://huggingface.co/datasets/Reallm-Labs/android_control_test)):
    ```bash
    huggingface-cli download --repo-type dataset --resume-download Reallm-Labs/android_control_test --local-dir ./
    ```
4.  Extract the downloaded data:
    ```bash
    tar -xzf android_control_test.tar.gz
    ```
5.  Run the evaluation scripts for high and low difficulty tasks:
    ```bash
    python android_control.py --model_path Reallm-Labs/InfiGUI-R1-3B --eval_type high --thinking
    python android_control.py --model_path Reallm-Labs/InfiGUI-R1-3B --eval_type low --thinking
    ```

## 📚 Citation Information

If you find this work useful, citations to the following papers are welcome:

```bibtex
@article{liu2025infigui,
  title={InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners},
  author={Liu, Yuhang and Li, Pengxiang and Xie, Congkai and Hu, Xavier and Han, Xiaotian and Zhang, Shengyu and Yang, Hongxia and Wu, Fei},
  journal={arXiv preprint arXiv:2504.14239},
  year={2025}
}
```

```bibtex
@article{liu2025infiguiagent,
  title={InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection},
  author={Liu, Yuhang and Li, Pengxiang and Wei, Zishu and Xie, Congkai and Hu, Xueyu and Xu, Xinchen and Zhang, Shengyu and Han, Xiaotian and Yang, Hongxia and Wu, Fei},
  journal={arXiv preprint arXiv:2501.04575},
  year={2025}
}
```

## 🙏 Acknowledgements
We would like to express our gratitude for the following open-source projects: [EasyR1](https://github.com/hiyouga/EasyR1), [VERL](https://github.com/volcengine/verl), [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory), and [Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL).
