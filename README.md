# yolov8

a simple demo of yolov8 on BDD100K.

## Data Preparation

**Download BDD100K**

BaiduNetDisk: https://pan.baidu.com/s/1fFSzGJt6Op4k7Gyo9QjtYA key: kuld

or our mini dataset `bdd100.zip`

```bash
unzip bdd100.zip
mkdir bdd100
mv images-mini bdd100
mv labels-mini bdd100
```

**Preprocess bdd100**

labels: json to xml, xml to txt

```bash
python json_xml.py
python xml_txt.py
```

build mydata

```bash
python build_data.py
```

create yml

```bash
touch mydata.yml
```

## Clone YOLOv8 Repo

```bash
git clone git@github.com:ultralytics/ultralytics.git
```

## Run Examples

run train example:

```bash
yolo task=detect mode=train model=yolov8n.pt data=mydata.yml batch=32 epochs=10 imgsz=640 workers=10 device=0
```

```
Ultralytics YOLOv8.2.27 🚀 Python-3.9.19 torch-2.3.0+cu121 CUDA:0 (NVIDIA A100-PCIE-40GB, 40377MiB)
engine/trainer: task=detect, mode=train, model=yolov8n.pt, data=mydata.yml, epochs=10, time=None, patience=100, batch=32, imgsz=640, save=True, save_period=-1, cache=False, device=0, workers=10, project=None, name=train2, exist_ok=False, pretrained=True, optimizer=auto, verbose=True, seed=0, deterministic=True, single_cls=False, rect=False, cos_lr=False, close_mosaic=10, resume=False, amp=True, fraction=1.0, profile=False, freeze=None, multi_scale=False, overlap_mask=True, mask_ratio=4, dropout=0.0, val=True, split=val, save_json=False, save_hybrid=False, conf=None, iou=0.7, max_det=300, half=False, dnn=False, plots=True, source=None, vid_stride=1, stream_buffer=False, visualize=False, augment=False, agnostic_nms=False, classes=None, retina_masks=False, embed=None, show=False, save_frames=False, save_txt=False, save_conf=False, save_crop=False, show_labels=True, show_conf=True, show_boxes=True, line_width=None, format=torchscript, keras=False, optimize=False, int8=False, dynamic=False, simplify=False, opset=None, workspace=4, nms=False, lr0=0.01, lrf=0.01, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=7.5, cls=0.5, dfl=1.5, pose=12.0, kobj=1.0, label_smoothing=0.0, nbs=64, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, bgr=0.0, mosaic=1.0, mixup=0.0, copy_paste=0.0, auto_augment=randaugment, erasing=0.4, crop_fraction=1.0, cfg=None, tracker=botsort.yaml, save_dir=runs/detect/train2
runOverriding model.yaml nc=80 with nc=10

                   from  n    params  module                                       arguments                
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]            
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]           
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]        
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]           
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]        
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]          
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]      
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]         
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]      
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]            
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']     
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                      
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]            
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']     
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                      
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]             
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]           
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                      
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]            
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]         
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                      
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]            
 22        [15, 18, 21]  1    753262  ultralytics.nn.modules.head.Detect           [10, [64, 128, 256]]     
Model summary: 225 layers, 3012798 parameters, 3012782 gradients, 8.2 GFLOPs

...

10 epochs completed in 0.044 hours.
Optimizer stripped from runs/detect/train2/weights/last.pt, 6.2MB
Optimizer stripped from runs/detect/train2/weights/best.pt, 6.2MB

Validating runs/detect/train2/weights/best.pt...
Ultralytics YOLOv8.2.27 🚀 Python-3.9.19 torch-2.3.0+cu121 CUDA:0 (NVIDIA A100-PCIE-40GB, 40377MiB)
Model summary (fused): 168 layers, 3007598 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████|
                   all        692      12444      0.559      0.203      0.201     0.0987
                   car        684       6906      0.564       0.45      0.471      0.251
                   bus         97        120       0.41      0.458      0.367       0.22
                person        223        956      0.422      0.243      0.241     0.0838
                  bike         58        118      0.372     0.0424     0.0656      0.027
                 truck        187        265       0.41      0.357      0.307      0.172
                 motor         21         34          1          0     0.0294     0.0129
                 rider         42         54          1          0     0.0374     0.0152
          traffic sign        562       2320      0.518        0.2      0.212      0.087
         traffic light        382       1671      0.337     0.0738     0.0755     0.0196
Speed: 0.3ms preprocess, 1.1ms inference, 0.0ms loss, 0.7ms postprocess per image
Results saved to runs/detect/train2
💡 Learn more at https://docs.ultralytics.com/modes/train
```

run valid example:

```bash
yolo task=detect mode=val model=runs/detect/train2/weights/best.pt data=mydata.yml device=0
```

```
Ultralytics YOLOv8.2.27 🚀 Python-3.9.19 torch-2.3.0+cu121 CUDA:0 (NVIDIA A100-PCIE-40GB, 40377MiB)
Model summary (fused): 168 layers, 3007598 parameters, 0 gradients, 8.1 GFLOPs
val: Scanning /home/wangyf/yolov8/mydata/valid/labels.cache... 692 images, 0 backgrounds, 0 corrupt: 100%|█
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████|
                   all        692      12444      0.563      0.202      0.201     0.0992
                   car        684       6906      0.568       0.45       0.47      0.251
                   bus         97        120      0.411      0.458      0.369      0.222
                person        223        956      0.431       0.24      0.241     0.0849
                  bike         58        118      0.374     0.0424     0.0683     0.0281
                 truck        187        265      0.412      0.355      0.307      0.173
                 motor         21         34          1          0     0.0295     0.0126
                 rider         42         54          1          0     0.0359     0.0148
          traffic sign        562       2320      0.525      0.201      0.214     0.0873
         traffic light        382       1671      0.343     0.0724     0.0754     0.0195
Speed: 0.2ms preprocess, 2.5ms inference, 0.0ms loss, 2.5ms postprocess per image
Results saved to runs/detect/val
💡 Learn more at https://docs.ultralytics.com/modes/val
```


## Reference:

- 使用YOLOV7训练BDD100K数据集（数据格式转化+训练全流程）：http://t.csdnimg.cn/C1yDz
- yolov5训练BDD100K自动驾驶数据集+pyqt5前端检测界面：http://t.csdnimg.cn/MfxIA
- YOLOv8 数据集训练参数详解：http://t.csdnimg.cn/YwqwH
- 数据集下载：https://pan.baidu.com/s/1fFSzGJt6Op4k7Gyo9QjtYA 提取码 kuld
- 官方代码库：https://github.com/ultralytics/ultralytics
