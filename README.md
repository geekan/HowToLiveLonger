# 程序员延寿指南

[![CN doc](https://img.shields.io/badge/文档-中文版-blue.svg)](README.md)
[![EN doc](https://img.shields.io/badge/document-English-blue.svg)](README_en.md)

- [1. 术语](#1-术语)
- [2. 目标](#2-目标)
- [3. 关键结果](#3-关键结果)
- [4. 分析](#4-分析)
- [5. 行动](#5-行动)
- [6. 证据](#6-证据)
  - [6.1. 输入](#61-输入)
    - [6.1.1. 固体](#611-固体)
    - [6.1.2. 液体](#612-液体)
    - [6.1.3. 气体](#613-气体)
    - [6.1.4. 光照](#614-光照)
    - [6.1.5. 药物](#615-药物)
  - [6.2. 输出](#62-输出)
    - [6.2.1. 挥拍运动](#621-挥拍运动)
    - [6.2.2. 走路](#622-走路)
    - [6.2.3. 刷牙](#623-刷牙)
    - [6.2.4. 泡澡](#624-泡澡)
    - [6.2.5. 做家务（老年男性）](#625-做家务老年男性)
    - [6.2.6. 睡眠](#626-睡眠)
  - [6.3. 上下文](#63-上下文)
    - [6.3.1. 情绪](#631-情绪)
    - [6.3.2. 贫富](#632-贫富)
    - [6.3.3. 体重](#633-体重)
    - [6.3.4. 新冠](#634-新冠)

---

### 1. 术语

* ACM: All-Cause Mortality / 全因死亡率

### 2. 目标

* 稳健地活得更久

### 3. 关键结果

* 降低66.67%全因死亡率
* 增加\~20年预期寿命
* ~~维持多巴胺于中轴~~

### 4. 分析

* 主要参考：对ACM的学术文献相对较多，可以作为主要参考
* 增加寿命与ACM关系非线性：显然增加寿命与ACM关系是非线性函数，这里假设 `DeltaLifeSpan=(1/(1+DeltaACM)-1)*10`（DeltaACM为ACM变化值；公式欢迎优化）
* 变量无法简单叠加：显然各个变量之间并不符合独立同分布假设，变量之间的实际影响也并不明确
* 存在矛盾观点：所有的证据都有文献/研究对应，但注意到：有些文献之间有显著矛盾的观点（如对于碳水摄入比例的矛盾）；有些文献存在较大争议（如认为22点前睡觉会提升43%全因死亡率）
* 研究仅表达相关：所有文献表明的更多是相关而非因果，在阅读时要考虑文献是否充分证明了因果 —— 如某文献表明了日均>=7000步的人有显著低的全因死亡率。但步数少的人可能包含更多长期病患，如果没有合理的排除这块数据，那此文献调查失真

### 5. 行动

* 输入
  * 固体：吃白肉（-11%\~-3% ACM）、蔬果为主（-26%\~-17% ACM），多吃辣（-23% ACM），多吃坚果（-27%\~-4% ACM），*少吃蛋黄（否则+7% ACM/0.5颗/天）（存在争议）*，中量碳水、多吃植物蛋白（-10% ACM），少吃超加工食物（-62%\~-18%）
  * 液体：喝咖啡（-22%\~-12% ACM），喝牛奶（-17%\~-10% ACM），喝茶（-15%\~-8% ACM），少喝或不喝甜味饮料（否则每天一杯+7% ACM，+多巴胺），戒酒或每周100g（纯酒精量(g)=饮酒量(ml)×酒精浓度(%)×酒精密度0.8g/ml）内（否则+\~50% ACM，无上限）
  * 气体：不吸烟（否则+~50% ACM，-12\~-11年寿命）
  * 光照：晒太阳（-~40% ACM）
  * 药物：二甲双胍（糖尿病人相比正常人可以+3年）、复合维生素（-8%癌症风险）、亚精胺（-60%\~-30% ACM）、葡萄糖胺（-39% ACM）
* 输出
  * 运动：每周3次45分钟挥拍运动（-47% ACM）
  * 日常：刷牙（-25% ACM）
  * 睡眠：每天睡7小时全因死亡率最低；且22-24点间最好，*早睡+43% ACM，晚睡+15% ACM（存在争议）*
* 上下文
  * 体重：减肥（-54% ACM）

### 6. 证据

#### 6.1. 输入

##### 6.1.1. 固体

* 白肉
  * [JAMA子刊：食用红肉和加工肉类会增加心脏病和死亡风险！鱼肉和家禽肉则不会](https://zhuanlan.zhihu.com/p/268401670)
    * 出处：[Associations of Processed Meat, Unprocessed Red Meat, Poultry, or Fish Intake With Incident Cardiovascular Disease and All-Cause Mortality](https://jamanetwork.com/journals/jamainternalmedicine/articlepdf/2759737/jamainternal_zhong_2020_oi_190112.pdf)
    * 增加红肉摄入与死亡风险相关。八年内平均每天增加至少半份红肉摄入（半份红肉相当于14g加工红肉或40g非加工红肉）的调查对象，在接下来八年内全因死亡风险增加10％（HR, 1.10; 95%CI, 1.04-1.17）；每周吃两份红肉或加工肉类（但不包括家禽或鱼类）会使全因死亡风险增加3%
    * ![红肉](https://user-images.githubusercontent.com/2707039/163703960-6f321de5-4daa-4ea5-95b9-af9c96f1c1bc.jpg)
  * [红肉和白肉最大的区别是什么？为啥要这么分呢？](https://www.zhihu.com/question/67223570/answer/809785380)
* 蔬果
  * [每年54万人死亡，竟是因为水果吃得少！？这已成十大死亡因素之一！](https://www.sohu.com/a/322360740_164924)
    * 出处：[Estimated Global, Regional, and National Cardiovascular Disease Burdens Related to Fruit and Vegetable Consumption: An Analysis from the Global Dietary Database (FS01-01-19) ](https://academic.oup.com/cdn/article-abstract/3/Supplement_1/nzz028.FS01-01-19/5516583)
    * 每天摄入200克新鲜水果可使死亡率降低17%，糖尿病大血管并发症（如中风、缺血性心脏病等）风险降低13%，及糖尿病小血管并发症（如糖尿病肾病、糖尿病眼病、糖尿病足病等）风险降低28%
  * [《自然》子刊：每天二两西兰花，健康长寿都有啦！分析近6万人23年的数据发现，吃含黄酮类食物与死亡风险降低20%相关丨临床大发现](https://mp.weixin.qq.com/s/E6BAi-Vnhr1jXBm0Pys2ZQ)
    * 出处：[Flavonoid intake is associated with lower mortality in the Danish Diet Cancer and Health Cohort](https://www.nature.com/articles/s41467-019-11622-x)
    * 吃含黄酮类食物与死亡风险降低20%相关
    * ![黄酮](https://user-images.githubusercontent.com/2707039/163703969-42e64f88-e727-4e7d-85f2-07a92e29b613.jpg)
    * Bondonno博士说道“吃不同蔬菜、水果补充，不同种类的黄酮类化合物是很重要的，这很容易通过饮食实现：一杯茶、一个苹果、一个橘子、100克蓝莓，或100克西兰花，就能提供各种黄酮类化合物，并且总含量超过500毫克。
* 辣椒
  * [辣椒成死亡克星？据调研，常吃辣患病死亡风险可降低61%](https://3g.163.com/dy/article/F6Q7I1ME053228ZU.html)
    * 出处1：[Chili pepper consumption and mortality in Italian adults](https://www.sciencedirect.com/science/article/pii/S0735109719382063)
	* 出处2：[The Association of Hot Red Chili Pepper Consumption and Mortality: A Large Population-Based Cohort Study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169876)
    * 2017年Plos One 的另一项来自美国的研究以16179名，年龄在18岁以上的人群为对象，并对其进行了高达19年的随访，发现在4946例死亡患者中，食用辣椒的参与者的全因死亡率为21.6％，而未食用辣椒的参与者的全因死亡率为33.6％。相较于不吃辣或很少吃（少于每周两次）的人群，每周吃辣＞4次的人群总死亡风险降低23%，心血管死亡风险降低34%。
* 鸡蛋
  * [每天多吃半个蛋，增加7%的全因和心血管死亡风险？](https://m.thepaper.cn/baijiahao_11540780)
    * 出处：[NIH-AARP工作主页](https://dietandhealth.cancer.gov/)、[Egg and cholesterol consumption and mortality from cardiovascular and different causes in the United States: A population-based cohort study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7872242/)
    * 每天多吃半个蛋，增加7%的全因和心血管死亡风险？在假设性替代分析中，研究者发现，用等量的蛋清/鸡蛋替代物、家禽、鱼、乳制品、坚果和豆类分别替代半只全蛋（25克/天）可以降低6%、8%、9%、7%、13%和10%的全因死亡率。
	*[鸡蛋](https://raw.githubusercontent.com/qhy040404/Image-Resources-Repo/master/pmed.1003508.g002.jpg)
* 坚果
  * [哈佛20年研究：吃核桃的人更长寿，显著减少全因死亡，延长寿命](https://www.163.com/dy/article/GKVOMMMF05148PF4.html)
    * 出处：[Association of Walnut Consumption with Total and Cause-Specific Mortality and Life Expectancy in US Adults](https://www.mdpi.com/2072-6643/13/8/2699/pdf)
    * 通过分析发现，经常食用核桃可以延长寿命，降低心血管疾病死亡风险。比起不吃核桃，每周食用核桃5份以上（1份28克）的健康预期寿命延长1.3岁，全因死亡风险降低14%，心血管疾病死亡率降低25%。
  * [研究：每日食生坚果，死亡率降20%](https://zhuanlan.zhihu.com/p/44454030)
    * 出处1：[Association of nut consumption with total and cause-specific mortality](https://www.nejm.org/doi/full/10.1056/NEJMoa1307352)
    * 出处2：[APG_Health-&-Nutrition-Research-Brochure_DEC-19-18](https://americanpistachios.cn/sites/china/files/inline-files/APG_Health-%26-Nutrition-Research-Brochure_DEC-19-18.pdf)
    * 研究人员发现，每周吃树坚果低于1盎司份量的人，死亡率降低7％。而每周吃了1盎司份量的人，减少11％的死亡率；每周吃2份量的人，减低13％；每周5至6份量者，减少了15％；一周7份以上的人，死亡率则减少20％。
    * 另外两篇发表在《公共科学图书馆在线期刊》(Public Library of Science Online Journal)和《生物医学中心》(BioMed Central)上的医学预科研究论文，展示了试验开始时的横断面数据。这两项研究都评估了7,216名对象，以及他们食用坚果的频率和数量之间的关系。那些每周食用三份以上坚果(包括开心果)的研究对象的死亡率降低39%。
* 钠（存有大量争议）
  * [Eur Heart J：钠摄入量与预期寿命、全因死亡率的关系](https://nursing.medsci.cn/article/show_article.do;jsessionid=A34E8A33918A152CB55BDD2E5FB1798D?id=afe720486ee7)
    * 出处：[Messerli F H, Hofstetter L, Syrogiannouli L, et al. Sodium intake, life expectancy, and all-cause mortality[J]. European heart journal, 2021, 42(21): 2103-2112.](https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC8169157&blobtype=pdf)
    * ![ehaa947f6](https://user-images.githubusercontent.com/2707039/164894778-9710f18d-e055-4f62-bdcb-618687771d77.jpeg)
    * 在该分析所包含的181个国家中，研究人员发现钠摄入量与出生时的健康预期寿命（β=2.6年/克每日钠摄入量，R<sup>2</sup>=0.66，P<0.001）和60岁时的健康预期寿命（β=0.3年/克每日钠摄入量，R<sup>2</sup>=0.60，P=0.048）之间存在正相关关系，但与非传染性疾病死亡（β=17次事件/克每日钠摄入量，R<sup>2</sup>=0.43，P=0.100）无关。相反，全因死亡率与钠摄入量成负相关（β=−131次事件/克每日钠摄入量，R<sup>2</sup>=0.60，P<0.001）。在仅限于46个收入最高国家的敏感性分析中，钠摄入量与出生时的健康预期寿命呈正相关（β=3.4年/克每日钠摄入量，R<sup>2</sup>=0.53，P<0.001），而与全因死亡率（β=−168次事件/克每日钠摄入量，R<sup>2</sup>=0.50，P<0.001）呈负相关。
    * 该（大范围）研究认为更多的钠摄入与显著更低的全因死亡率有关
    * [针对该论文的延伸解读和讨论：A Fresh Foray in the Salt Wars: Life Expectancy Higher With Greater Sodium Intake](https://www.tctmd.com/news/fresh-foray-salt-wars-life-expectancy-higher-greater-sodium-intake)
  * [NEJM/Lancet：不要吃太多盐，中国饮食所致心血管病和癌症死亡全球第一，吃低钠盐可降低全因死亡率](https://ibook.antpedia.com/x/669028.html)
    * 但也有多项研究认为用低钠盐可以降低一系列疾病的发生概率，对全因死亡率的减少有积极影响
* 碳水（存有大量争议）
  * [低碳生酮饮食（四）碳水化合物与长期死亡率](https://zhuanlan.zhihu.com/p/137815934)
    * 出处：The Lancet Public Health - [Dietary carbohydrate intake and mortality: a prospective cohort study and meta-analysis](https://www.sciencedirect.com/science/article/pii/S246826671830135X)
    * 碳水越低，寿命越短；碳水越高，寿命也轻微缩短；碳水50%左右（其实按照一般的说法，这也算高碳水）是最长寿命区间 
    * ![碳水](https://user-images.githubusercontent.com/2707039/163703985-a2e2f8ac-101a-4f3c-903b-6850507f144b.jpg)
  * [最强营养搭配！BMJ：这么吃，心血管疾病和死亡风险更低](https://www.chinacdc.cn/gwxx/202003/t20200323_214639.html)
* 槟榔
  * [如何看待槟榔嚼出来的癌症？槟榔致癌风险究竟有多大？ - 丁香医生的回答 - 知乎](https://www.zhihu.com/question/312784161/answer/603370131)
    * 出处：Chewing Betel Quid and the Risk of Metabolic Disease, Cardiovascular Disease, and All-Cause Mortality: A Meta-Analysis(https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0070679)
    * 嚼槟榔会增加21%的全因死亡率
* 热量限制
  * [怎么看待BBC《进食、断食与长寿》？](https://www.zhihu.com/question/31395511)
    * 限制卡路里动物实验：CR（热量限制，即少吃）延迟了恒河猴的多种疾病发病和死亡率，与CR动物相比，正常喂养的猴子的各种疾病患病风险增加2.9倍，死亡风险增加3.0倍。
    * ![热量限制-恒河猴](https://user-images.githubusercontent.com/2707039/163703988-8767185b-326a-4783-b2e2-f190322bb7d6.jpg)
* 综合
  * [最强营养搭配！BMJ：这么吃，心血管疾病和死亡风险更低](https://www.chinacdc.cn/gwxx/202003/t20200323_214639.html)
  * [Associations of fat and carbohydrate intake with cardiovascular disease and mortality: prospective cohort study of UK Biobank participants](https://doi.org/10.1136/bmj.m688)
    * 通过对这些参与者的数据进行分析，研究人员发现碳水化合物（糖、淀粉和纤维）和蛋白质的摄入与全因死亡率呈非线性关系，而脂肪则与全因死亡率呈线性相关。其中，较高的糖分摄入与全因死亡风险和患心血管疾病的风险较高均有关联，而较高的饱和脂肪酸摄入与全因死亡风险较高有关。
    * 图1：各种营养元素与全因死亡之间的关系
    * ![各种营养元素与全因死亡之间的关系](https://user-images.githubusercontent.com/2707039/163702022-8c2bfea9-ed5d-4fe0-8ead-e8740014b92b.jpg)
    * 图2：各种营养元素与心血管疾病之间的关系
    * ![各种营养元素与心血管疾病之间的关系](https://user-images.githubusercontent.com/2707039/163702084-97fb4a03-707c-475d-b88e-6fe2f8e87f92.jpg)
    * **进一步研究表明，在所有的饮食模式中，全因死亡率风险最低的饮食方式为：10-30g高纤维、14-30%蛋白质、10-25%单不饱和脂肪酸、5%-7%多不饱和脂肪酸以及20%-30%淀粉摄入。**
    * **最优能量来源配比：<24%淀粉，15%-17%蛋白质，>15%单不饱和脂肪酸，<15%糖，6%饱和脂肪酸，6%多不饱和脂肪酸，30g+高纤维**
  * [BMJ | 常吃薯片汉堡巧克力等食品，平均死亡年龄仅仅为58岁，死亡风险剧增](https://med.ckcest.cn/details.html?id=5183272274855936&classesEn=news)
    * [Rico-Campà A, Martínez-González M A, Alvarez-Alvarez I, et al. Association between consumption of ultra-processed foods and all cause mortality: SUN prospective cohort study[J]. bmj, 2019, 365.](https://www.bmj.com/content/365/bmj.l1949.full)
    * [Srour B, Fezeu L K, Kesse-Guyot E, et al. Ultra-processed food intake and risk of cardiovascular disease: prospective cohort study (NutriNet-Santé)[J]. bmj, 2019, 365.](https://www.bmj.com/content/365/bmj.l1451)
    * [Lawrence M A, Baker P I. Ultra-processed food and adverse health outcomes[J]. bmj, 2019, 365.](https://www.researchgate.net/profile/Phillip-Baker-5/publication/333483796_Ultra-processed_food_and_adverse_health_outcomes/links/5f0c646ca6fdcc2f32336a95/Ultra-processed-food-and-adverse-health-outcomes.pdf)

##### 6.1.2. 液体

* 牛奶
  * [《柳叶刀》调研21个国家13万人：每天1斤牛奶或酸奶，心血管死亡风险下降23%](https://www.sohu.com/a/253940257_419768)
  * 出处：[Association of dairy intake with cardiovascular disease and mortality in 21 countries from five continents (PURE): a prospective cohort study](http://mdrf-eprints.in/1114/1/Association_of_dietary_patterns_and_dietary_diversity_with_cardiometabolic_disease_risk_factors.pdf)
  * 与不食用乳制品的人相比，每天摄入两份乳制品（一份指244克牛奶/酸奶，15克奶酪或5克黄油）的人，**全因死亡风险下降了17%**，心血管死亡风险下降23%，中风风险下降33%
* 茶
  * [10万中国人随访7年发现，每周喝三次茶与全因死亡风险降低15%，预期寿命增加1.26年相关 ](https://www.jianshu.com/p/5461a205cf95?utm_campaign=hugo)
  * 出处：[Tea consumption and the risk of atherosclerotic cardiovascular disease and all-cause mortality: The China-PAR project](https://www.researchgate.net/profile/Fangchao-Liu-4/publication/338483323_Tea_consumption_and_the_risk_of_atherosclerotic_cardiovascular_disease_and_all-cause_mortality_The_China-PAR_project/links/5e55e5e94585152ce8efe511/Tea-consumption-and-the-risk-of-atherosclerotic-cardiovascular-disease-and-all-cause-mortality-The-China-PAR-project.pdf)
  * [中国成年人饮茶与死亡风险的前瞻性关联研究](http://rs.yiigle.com/CN112338202202/1351516.htm)
  * 纳入分析的438 443例研究对象随访11.1年共发生死亡34 661例。与从不饮茶者相比，当前非每日饮茶者和每日饮茶者全因死亡HR值（95%CI）依次为0.89（0.86-0.91）和0.92（0.88-0.95）。分性别分析显示，饮茶对全因死亡风险的保护作用主要见于男性（交互P<0.05）
* 无糖（甜味）饮料
  * [「无糖饮料使死亡风险增加 26 %」，是真的吗？](https://www.zhihu.com/question/418598272/answer/1450648364)
    * 相比于软饮料摄入量＜1杯/月的参与者，混合软饮料摄入≥1杯/天的参与者死亡风险增加18%，而**摄入含糖软饮料或无糖软饮料会令死亡风险分别增加11%和27%。**
    * ![饮料](https://user-images.githubusercontent.com/2707039/163704346-e7d92e7f-eba5-4673-8f15-3a96782c2e32.png)
  * [Association Between Soft Drink Consumption and Mortality in 10 European Countries](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2749350)
* 有糖饮料
  * [可乐和奶茶，增加全因死亡率高达62%！果汁降低免疫力，影响肝代谢！含糖饮料那些事](https://zhuanlan.zhihu.com/p/400746073)
    * 每天1杯含糖饮料增加7%全因死亡率，2杯21%
    * 在34年的随访中，研究人员发现，相比那些一个月喝1杯或者更少含糖饮料的人，每天喝2杯的人总体死亡风险升高了21%，心血管疾病死亡风险升高了31%，癌症死亡风险上升了16%。
    * 只要每天多喝一杯含糖饮料，总体死亡风险将增加7%，心血管疾病的风险将增加10%，癌症相关的死亡风险将16%。
    * 发表在国际顶级期刊《BMJ》上的一篇论文就证明了含糖饮料会在增加患癌风险，当然这篇文章验证的不仅仅是果汁，奶茶也有份——和含糖饮料相关的总体患癌风险要高出通常值18%，100%的鲜榨果汁也会使得整体的患癌风险上升12%。
* 果汁
  * [JAMA子刊：100%纯果汁可能比含糖饮料更危险](https://zhuanlan.zhihu.com/p/66513350)
    * 每天多摄入一份12盎司的含糖饮料，全因死亡率风险增加11%；
    * 每天多摄入一份12盎司的果汁，全因死亡率风险增加24%。
* 咖啡
  * [重磅！多篇研究证实喝咖啡与人群全因死亡率降低直接相关](https://news.bioon.com/article/6725420.html)
  * [科普 | 喝咖啡又多了一个新理由：降低死亡率！ ](https://www.sohu.com/a/439412995_100003595)
  * [地中海成年人咖啡消耗量及全因，心血管疾病和癌症的死亡率](https://fanyi.pdf365.cn/help/249)
    * 在最近的荟萃分析中，该研究包括来自不同国家的40项研究和3,852,651名受试者。在这项荟萃分析显示，咖啡摄入量与各种原因的死亡率，CVD和癌症死亡率之间存在非线性关系，每天摄入两杯咖啡的癌症死亡率最低(RR = 0.96)，CVD最低的死亡率，每天2.5杯(RR= 0.83)，全天最低死亡率为每天3.5杯(RR= 0.85)，并且随着咖啡消费量的增加，死亡率没有进一步降低或增加
* 亚精胺
  * [Science：科学背书！从精液中发现的亚精胺，竟然有着抗衰老、抗癌、保护心血管和神经、改善肥胖和2型糖尿病等逆天神效](https://www.medsci.cn/article/show_article.do?id=420d12904103)
  * [饮食中亚精胺摄入量高会降低死亡率](https://zhuanlan.zhihu.com/p/388942219)

##### 6.1.3. 气体

* 吸烟
  * [即使是低强度吸烟，也增加死亡风险！](https://www.medsci.cn/article/show_article.do?id=02ca2083319b)
    * 研究发现：在42 416名男性和86 735名女性（年龄在35-89岁之间，以前没有患病）中，18 985名男性（45%）和18 072名女性（21%）目前吸烟，其中33%的男性吸烟者和39%的女性吸烟者并不每天吸烟。8866名男性（21%）和53 912名女性（62%）从不吸烟。在随访期间，与从不吸烟相比，每天<10支烟或每天≥10支烟的全因死亡率危险比分别为1.17（95%置信区间1.10-1.25）和1.54（1.42-1.67）。无论年龄或性别，危险比相似。与每日吸烟关系最密切的疾病是呼吸道癌症、慢性阻塞性肺病和胃肠道及血管疾病。在招募时已经戒烟的人的死亡率低于现在每天吸烟者。
    * 吸烟者平均减少寿命11-12年
  * [吸烟让人过瘾是什么原理？有节制的吸烟依旧有害吗？](https://www.zhihu.com/question/24846224/answer/1719798177)

##### 6.1.4. 光照

* 晒太阳
  * [晒太阳和死亡率的关系，如何科学，安全的晒太阳？
](https://zhuanlan.zhihu.com/p/76301306)
    * 丹麦一项长达26年的研究发现，多晒太阳能显著延长寿命，即使是由于过度暴晒诱发皮肤癌的患者，平均寿命也比普通人长了6岁。

##### 6.1.5. 药物

* NMN
* 二甲双胍
  * [“胍”吹必看 丨我就是神药——二甲双胍](https://zhuanlan.zhihu.com/p/419202902)
    * 二甲双胍不仅在多种肿瘤、心血管疾病及糖尿病中发挥保护作用，而且在肥胖、肝病、肾病及衰老方面也大放异彩。
  * [二甲双胍2020最值得了解的“吃瓜”大新闻——护胃、健脑、抗衰、防癌还是致癌？](https://zhuanlan.zhihu.com/p/357807109)
  * [二甲双胍真的那么神吗？美研究：父亲服用二甲双胍或致子女有缺陷](https://baijiahao.baidu.com/s?id=1729999374705305768)
  * ![二甲双胍](https://user-images.githubusercontent.com/2707039/163702325-5d427542-9ae5-4311-8979-d0d326a9832f.jpg)
  * 不良反应
    * 作为一种使用近百年的药物，二甲双胍的不良反应已经非常明确，常见的有：维生素B12缺乏（7%-17.4%），胃肠道不良反应（最高53%），疲倦（9%），头痛（6%）；严重但不常见的不良反应包括乳酸酸中毒、肝损伤；也有研究表明可能对胎儿致畸
* 复合维生素
  * [服用复合维生素可降低癌症危险8%，其他效果并不显著](https://health.qq.com/a/20121023/000026.htm)
* 葡萄糖胺
  * [神奇！氨糖降低心血管死亡率65%，与定期运动效果相当](https://www.sohu.com/a/436372221_120873241)
  * 美国西弗吉尼亚大学最新研究发现 氨糖（软骨素） 可以降低心血管死亡率65%，降低总体死亡率39%，效果与坚持定期运动相对
  * 该研究使用1999年至2010年，16,686名成年人的国家健康和营养检查(NHANES)数据，参与者的中位追踪时间为107个月，而其中有648位参与者定期且每服用日500-1000毫克的葡萄糖胺/软骨素一年以上。
* 亚精胺
  * [Science：科学背书！从精液中发现的亚精胺，竟然有着抗衰老、抗癌、保护心血管和神经、改善肥胖和2型糖尿病等逆天神效](https://www.medsci.cn/article/show_article.do?id=420d12904103)
  * 亚精胺是最容易从人体肠道吸收的多胺。许多的食物中都含有大量的亚精胺，例如新鲜的青椒、小麦胚芽、花椰菜、西兰花、蘑菇和各种奶酪，尤其在纳豆等大豆制品、香菇和榴莲中含量更高。在本实验中，研究人员选择了829位年龄在45-84岁之间的参与者进行了为期20年的随访，分析了饮食中亚精胺摄入量与人类死亡率之间的潜在关联。
  * 研究发现，女性的亚精胺摄入量高于男性，并且摄入量都会随着年龄的增长而下降。亚精胺的主要来源是全谷物（占13.4%）、苹果和梨（占13.3%）、沙拉（占9.8%）、芽菜（占7.3%）和马铃薯（占6.4%）。研究根据亚精胺摄入量将人群分为三组，低摄入量组（<62.2 µmol / d）、中摄入量组（62.2–79.8 µmol / d）和高摄入量组（> 79.8 µmol / d）。随访期间共记录了341例死亡，其中血管疾病137例，癌症94例，其他原因110例。经计算低中高三组的粗略死亡率分别为40.5%、23.7%和15.1%，这些数据表明亚精胺摄入量与全因死亡率之间的负相关关系显著。随着逐步对年龄、性别和热量的比例进行调整，这种相关关系依然显著。
* 综合
  * [《自然》子刊深度综述：如何开发抗衰老药](https://zhuanlan.zhihu.com/p/145495570)
  * ![如何开发抗衰老药](https://user-images.githubusercontent.com/2707039/163702474-205baeec-f0ce-4e8d-96a4-36efe47534de.jpg)

#### 6.2. 输出

##### 6.2.1. 挥拍运动

* [哪种运动性价比最高？权威医学杂志“柳叶刀”给出答案了 ](https://www.sohu.com/a/535581770_121124216)
  * 一周三次，每次45-60分钟，挥拍运动，降低~47%全因死亡率
  * 羽毛球、乒乓球、网球等都算挥拍运动，但由于西化研究背景，可能指网球更多。这隐式的表达了全身锻炼更为重要

##### 6.2.2. 走路

* [走路降低全因死亡率超过50%！每天走多少步最合适？《JAMA》子刊超10年研究告诉你答案](http://www.shcell.org/219/3571.html)
  * ![走路降低全因死亡率](https://user-images.githubusercontent.com/2707039/163704147-afec1c79-799b-4db8-b547-1a2431d504c9.jpg)
  * 注1：这项研究参与者的平均年龄为45.2岁
  * 注2：平均步数的多少与职业有关，此项研究仅表明相关性，还没有更深度的因果分析

##### 6.2.3. 刷牙

* [50万国人研究证实：不好好刷牙，致癌！血管疾病也会增多！](https://www.cn-healthcare.com/articlewm/20211209/content-1293760.html)
  * 经常不刷牙的人：癌症、慢性阻塞性肺病及肝硬化风险分别增加了9%、12%和25%，过早死亡风险增加25%。

##### 6.2.4. 泡澡

* [定期洗澡降低心血管疾病发作风险](https://www.cn-healthcare.com/article/20200326/content-533379.html)
  * 与每周一至两次泡澡或根本不泡澡相比，每天洗热水澡可以降低28%的心血管疾病总风险，降低26%的中风总风险，脑出血风险下降46%。而浴缸浴的频率与心源性猝死的风险增加无关。

##### 6.2.5. 做家务（老年男性）

* [Housework Reduces All-Cause and Cancer Mortality in Chinese Men](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061529)
  * 72岁之后男性每周做重型家务可以减少29%平均死亡率
  * 重型家务：吸尘、擦地板、拖地、擦洗窗户、洗车、搬动家具、搬煤气罐等等。
  * 轻型家务：掸灰尘、洗碗、手洗衣服、熨烫、晾衣服、做饭、买日用品等等。

##### 6.2.6. 睡眠

* [超30万亚洲人数据：每天睡几个小时最有益长寿？](https://med.sina.com/article_detail_103_1_105491.html)
  * 在男性中，与睡眠时长为7小时相比：睡眠持续时间≥10小时与全因死亡风险增加34%相关；
  * ![睡眠-男](https://user-images.githubusercontent.com/2707039/163704166-226b7ebb-92ce-4753-a3e7-77a87652a104.jpg)
  * 在女性中，与睡眠持续时间7小时相比：睡眠持续时间≥10小时与全因死亡风险增加48%相关；
  * ![睡眠-女](https://user-images.githubusercontent.com/2707039/163704169-c5c715aa-7130-403b-b0d1-ec34fab094d8.png)
* [颠覆认知！加拿大研究发现：早睡比熬夜或许更伤身，几点睡才好？](https://www.thepaper.cn/newsDetail_forward_14461799)
  * 其中一个结论为，就寝时间与全因死亡率的关联性强，过早睡觉和过晚睡觉都会影响健康，但是早睡增加的全因死亡率比晚睡增加的死亡率高，早睡增加了43%的死亡风险，而晚睡增加了15%的死亡风险。
  * 这项调查研究，还存在很多局限性，比如没有直接证明就寝时间与死亡的关系，仅仅说明相关性，通过参与人群自我报告统计睡眠时间，数据不够客观

#### 6.3. 上下文

##### 6.3.1. 情绪

* [悲观情绪与更高的全因死亡率和心血管疾病死亡率有关，但乐观情绪并不能起到保护作用](https://www.x-mol.com/paper/1288184397379059712/t?recommendPaper=1263704526086578176)
* [Pessimism is associated with greater all-cause and cardiovascular mortality, but optimism is not protective](https://www.nature.com/articles/s41598-020-69388-y?utm_source=xmol&utm_medium=affiliate&utm_content=meta&utm_campaign=DDCN_1_GL01_metadata_scirep)
  * 在1993-1995年间，一项针对50岁以上澳大利亚人健康的双胞胎研究中包括了生活取向测试（LOT），其中包含乐观和悲观的项目。平均20年后，参与者与来自澳大利亚国家死亡指数的死亡信息相匹配。在2,978名具有很多可用分数的参与者中，有1,068人死亡。生存分析测试了各种乐观因素和悲观情绪分数与任何原因，癌症，心血管疾病或其他已知原因的死亡率之间的关联。年龄调整后的悲观量表上的核心与全因和心血管疾病死亡率相关（每1个标准差单位的危险比，95％置信区间和p值1.134、1.065–1.207、8.85×10 –5和1.196、1.045–1.368、0.0093 ），但不会因癌症死亡。乐观得分与悲观得分之间的相关性很弱（年龄调整后的等级相关系数= − 0.176），但与总死亡率或特定原因死亡率没有显着相关性。反向因果关系（引起悲观情绪的疾病）是不可能的，因为在那种情况下，心血管疾病和癌症都会导致悲观情绪。

##### 6.3.2. 贫富

* [JAMA子刊：贫富差距真能影响寿命？这可能是真的！](https://www.cn-healthcare.com/articlewm/20210727/content-1246348.html)
  * 该研究使用1994-1996年第一次收集的数据，并通过生存模型来分析净资产和长寿之间的关联。结果显示，共收纳5414 名参与者，平均年龄为 46.7岁，包括 2766 名女性。较高的净资产与较低的死亡风险相关。特别是在兄弟姐妹和双胞胎中（n = 2490），在较高的净资产和较低的死亡率之间观察到类似的关联，表明拥有更多财富的兄弟姐妹或双胞胎比拥有更少财富的兄弟姐妹/双胞胎活得更久。

##### 6.3.3. 体重

* [JAMA子刊：减肥要趁早，才能有效降低死亡率风险](https://www.chinacdc.cn/gwxx/202009/t20200904_218959.html)
  * 对体重减轻的死亡率风险评估发现，体重从肥胖减轻到超重的成年人与稳定肥胖人群相比，全因死亡率降低了54％（危险比为0.46），然而从成年初期的超重减轻到中年以前的正常体重的人群的死亡率风险并未降低（风险比为1.12）。
  * ![Table3](https://raw.githubusercontent.com/qhy040404/Image-Resources-Repo/master/zoi200509t3_1596761185.02415.png)

##### 6.3.4. 新冠

* [Magnitude, demographics and dynamics of the effect of the first wave of the COVID-19 pandemic on all-cause mortality in 21 industrialized countries](https://www.nature.com/articles/s41591-020-1112-0.pdf)
  * 目前来看，新冠死亡率（美国）在1.5%左右，人均预期寿命减少了2年
* [如何看待美国CDC宣称新冠死亡人数被高估？](https://www.zhihu.com/question/510943670/answer/2308499719)
* [NVSS deaths](https://www.cdc.gov/nchs/nvss/deaths.htm)
