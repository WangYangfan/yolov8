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

## Clone Repo and run

```bash
git clone git@github.com:ultralytics/ultralytics.git
```

run train example:

```bash
yolo task=detect mode=train model=yolov8n.pt data=mydata.yml batch=32 epochs=10 imgsz=640 workers=10 device=0
```

run valid example:

```bash
yolo task=detect mode=val model=runs/detect/train2/weights/best.pt data=mydata.yml device=0
```

## Reference:
- 使用YOLOV7训练BDD100K数据集（数据格式转化+训练全流程）：http://t.csdnimg.cn/C1yDz
- yolov5训练BDD100K自动驾驶数据集+pyqt5前端检测界面：http://t.csdnimg.cn/MfxIA
- YOLOv8 数据集训练参数详解：http://t.csdnimg.cn/YwqwH
- 数据集下载：https://pan.baidu.com/s/1fFSzGJt6Op4k7Gyo9QjtYA 提取码 kuld
- 官方代码库：https://github.com/ultralytics/ultralytics
