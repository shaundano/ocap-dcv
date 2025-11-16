## ocap-elephant
This is a fork of ocap by the open-world-agents team that is set up to work on a VM, includes microphone capture, and is configured for automated graceful shutdown on Windows. Basically, it writes its process ID in a file, and then another python script can read it and send a signal interrupt, which is necessary to automate the shutdown of ocap.
 
 # ocap

[![ocap](https://img.shields.io/pypi/v/ocap?label=ocap)](https://pypi.org/project/ocap/) [![gstreamer-bundle](https://img.shields.io/conda/vn/open-world-agents/gstreamer-bundle?label=gstreamer-bundle)](https://anaconda.org/open-world-agents/gstreamer-bundle)

High-performance desktop recorder for Windows. Captures screen, audio, keyboard, mouse, and window events.

This project was first introduced and developed for the D2E project. For more details, see [D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI](https://worv-ai.github.io/d2e/) If you find this work useful, please cite our paper.

## What is ocap?

**ocap** (Omnimodal CAPture) captures all essential desktop signals in synchronized format. Records screen video, audio, keyboard/mouse input, and window events. Built for the _open-world-agents_ project but works for any desktop recording needs.

> **TL;DR**: Complete, high-performance desktop recording tool for Windows. Captures everything in one command.

https://github.com/user-attachments/assets/4e94782c-02ae-4f64-bb52-b08be69d33da

## Citation

Citing the original work:

```
@article{choi2025d2e,
  title={D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI},
  author={Choi, Suwhan and Jung, Jaeyoon and Seong, Haebin and Kim, Minchan and Kim, Minyeong and Cho, Yongjun and Kim, Yoonshik and Park, Yubeen and Yu, Youngjae and Lee, Yunsung},
  journal={arXiv preprint arXiv:2510.05684},
  year={2025}
}
```
