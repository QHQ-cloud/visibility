language:python

```python
# requirement：numpy、pytorch、tqdm、PIL,opencv、etc
# 此处未将class文件 与model.pkl文件加进来
# c3d.class文件夹下代表MOR_1A的22种类别,每一种类别都保存了许多能见度的图片，图片截取及处理见prepicture.py，（此处为简化处理）文件夹的名字即为类别
# 有图片之后，需要为图片打上标签，即每一张图片对应的类别（见label.py），并为此建立dataset，（见build_dataset）

# 有了数据之后，构建网络模型，此处采用resnet18,(百度之)，完成以后，即可训练（见train.py）


# eval.py 测试代码

# train.py会建立checkpoint,需要花时间训练之后才能得到，得到之后进行测试

#train.txt文件对应训练集 格式前半部分是图片数据，后半部分为类别，由label.py得到

# config.py 放置配置文件 比如学习率、device等

# model文件夹下即放置 训练好的权重文件（checkpoint）

# 预处理过程1：在prepicture.py中体现为：
1:根据视频数据，每一秒提取为1帧
2：在提取过程中，首先做resize处理，；类似于Word中对图片拉长...（处理为448*448像素）

3:448*448像素还是太大，进行crop，（裁剪为228*228），选取有代表性的区域
    
4：由于是彩色图片，进行灰度处理
# 预处理2：在bulid_dataset中的transform中体现，请查看源代码：
1：对图片进一步裁剪，（32*32）
2：对图片随机水平翻转
3：处理为tensor，这样才能在torch中运行


百度搜索resnet





```

### 总体流程

首先通过视频数据，切割为一帧一帧的图片，每秒为一帧，在切分过程中，作上述（预处理过程1）预处理，但是有了数据，还需要为数据打上标签，所以根据20_vis.his文件，选取MOR_1A为分类变量，（此处本应该做回归处理，但因为时间有限，只能做基础分类），一共有22个类别，为截取出来的每一张图片均打上标签。在打标签的过程中，划分训练集和测试集，按照（7:1）划分。打上标签以后，根据pytorch的设计原则，需要自己建立dataset，继承自torch.utils.data.Dataset,重写__len__方法，和__get_item__方法，建立图片与标签对应的数据集。在这里继续对图片做处理（预处理2）。之后，建立Dataloader迭代器，这样就可以将数据传入神经网络训练了。

训练采用的网络选取为resnet18,将训练集的数据传入网络，不断迭代，以期得到较高的准确率。训练过程中，每隔多少个epoch进行一次权重参数的保存。训练一段时间以后，就可以通过eval.py进行测试。查看准确率。如果训练集效果一般，测试集比较差，说明还需在原来保存的checkpoint上继续训练。如果训练很长时间，训练集出现较高准确率，但是测试集准确率较低，说明出现过拟合现象，需要重新调整模型，例如修改模型参数，修改模型结构等。



目录结构为:(prepicture.py在construction根目录下）

![1](D:\construction\1.png)

![2](D:\construction\2.png)

![3](D:\construction\3.png)







