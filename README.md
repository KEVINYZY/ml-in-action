## 学习资料

#### python篇

- [python3教程——runoob.com](http://www.runoob.com/python3/python3-tutorial.html)
- [python3教程——廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

#### 机器学习篇

- [scikit-learn 官方文档](http://scikit-learn.org/stable/index.html)
- [scikit-learn 特征处理方法](http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
- [numpy 官方文档 quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
- [matplotlib 画图库](https://matplotlib.org/)

#### 深度学习篇

- [原版github仓库](https://github.com/tensorflow/tensorflow)
- [中文版github](https://github.com/jikexueyuanwiki/tensorflow-zh)

#### 自然语言处理篇

本节大部分的内容摘自——[qhduan的ConversationalRobotDesign](https://github.com/qhduan/ConversationalRobotDesign)

流程细节：

1. 数据的输入，文字或者语音(可以通过第三方直接转成文字)
2. 文字处理：
    中文分词(jieba,hanlp)、
    实体识别(ner, wit.ai和api.ai)、
    意图识别(intent detection)
    对话可采用：命令式、模糊式；
    判断是否匹配的方法（levenshtein distance, word net, 2vec, lstm）

实践经验：

1. 易学易用的QA Pairs管理查询引擎，如怎么退货
2. 易学易用的对话模板生成管理，如每个商品或者分类咨询的固定话术
3. NLU内部组件，如intent classification意图识别, entity recognization实体识别, 人工分词
4. 机器人不准的时候，人工介入，如电话、邮件、IM
5. 对化状态跟踪dialogue state tracker 对话策略组件dialogue policy
6. 模拟程序(不了解这个模拟程序的作用)与评价系统
7. 良好的开发文档
8. 面对业务良好的培训文档
9. 自动训练程序
10. Attention机制，Residual RNN机制，Dropout机制
11. 实体词管理，系统词典、自定义词典，词典名字、词条、同义词管理等
12. 意图识别可以考虑优先级，实体词抽取，提示话术，默认值
13. Slotfilling 必须词条
14. 为方便操作可以添加快捷键，快捷回复。可以多参考ruyi.ai

关键技术与名词：

1. 对话系统(dialogue system / dialog system)， GUS对话系统(genial understander system)
2. 问答系统(question answering system), QA paris问答对、KBQA(knowledge based QA知识库问答)、Retrival based QA基于检索
3. 聊天机器人(chatbot)
4. 人工智能标记语言(AIML)
5. 深度学习聊天机器人(Sequence to Sequence)
6. 任务驱动式多轮对话(Spoken Dialogue System, SDS)

论文
A Non-Task-Oriented Mixture Model Dialog System
Daniel G. Bobrow, GUS, A Frame-Driven Dialog System, 1977

- [科大讯飞](http://www.aidaxue.com/)
- [百度度秘](https://www.leiphone.com/news/201709/RH5bLiHe35RwjC2j.html)
- [阿里小蜜介绍，效果可以去APP端自行体验](https://mp.weixin.qq.com/s/hTC62L1GFwsyC_EEdgNFXw?spm=a2c4e.11153940.blogcont108611.11.35f95fe6NoYkUc)
- [自己做聊天机器人](http://www.shareditor.com/blogshow?blogId=63)
- [conversational robot desing —— qhduan](https://github.com/qhduan/ConversationalRobotDesign)
- [聊天机器人：神经对话模型的实现与技巧](https://github.com/qhduan/ConversationalRobotDesign/tree/master/%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%EF%BC%9A%E7%A5%9E%E7%BB%8F%E5%AF%B9%E8%AF%9D%E6%A8%A1%E5%9E%8B%E7%9A%84%E5%AE%9E%E7%8E%B0%E4%B8%8E%E6%8A%80%E5%B7%A7)
- [AIML——rivescript](https://www.rivescript.com/)
- [AIML——superscript](https://github.com/superscriptjs/superscript)
- [AIML——chatscript](https://github.com/bwilcox-1234/ChatScript)
- [参考文档——微软对话系统技术挑战](https://www.microsoft.com/en-us/research/event/dialog-state-tracking-challenge/)
- [参考文档——剑桥对话系统组](http://dialogue.mi.eng.cam.ac.uk/)
- [参考文档——剑桥课件](http://mi.eng.cam.ac.uk/~mg436/LectureSlides/)
- [参考文档——Stanford 对话和语言处理](http://web.stanford.edu/~jurafsky/slp3/)
- [产品参考——国内——yige.ai](http://www.yige.ai/)
- [产品参考——国内——ruyi.ai](https://ruyi.ai/)
- [产品参考——国外——pandaorabots](https://home.pandorabots.com/en/)
- [产品参考——剑桥——pydial](http://www.camdial.org/pydial/)
- [开源实现——DeepPavlov](https://github.com/deepmipt/DeepPavlov)
- [开源实现——chatterBot](https://github.com/gunthercox/ChatterBot)
- [开源实现——buboqa](https://github.com/castorini/BuboQA)
- [得翻墙 api.ai](http://api.ai/)

#### 计算机视觉篇

- [图片资源库](http://blog.csdn.net/chaipp0607/article/details/71403797)
- [opencv学习网址](http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/tutorials.html)
- [yolo github]()
- [知乎专栏-YOLO：实时快速目标检测](https://zhuanlan.zhihu.com/p/25045711)
- [YOLO论文](https://arxiv.org/pdf/1506.02640.pdf)

## 书籍参考

- 《机器学习实战》
- 《数据科学入门》
- 《Python自然语言处理》
- 《数学之美》
- 《数字图像处理》- russ
- 《python计算机视觉》
- 《OpenCV3计算机视觉 python语言实现》
