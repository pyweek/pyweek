# Python每周挑战

用于提交 “Python每周挑战” 的答案

按如下结构提交代码：

```
pyweek/
.
├── week_1          // 第 1 周的挑战题目
│   ├── answers     // 答案提交文件夹
│   │   ├── 0       // 以数字0为名字的文件夹中是该次挑战评选出来的“参考答案”
│   │   ├── lisi
│   │   └── zhangsan              // **答题者应该只提交此目录及其内容，命名以自己github用户名为准**
│   │       ├── answer.py         // 必须有的主要答案代码
│   │       ├── readme.md         // 对答案的解释之类的
│   │       └── customlib.py      // 自己定义的辅助类、函数之类的，不必是这个名字
│   └── question    // 该次挑战的问题， 虽然博客上也有问题，但为了方便收藏也把题目再复制过来
│       └── question.md
└── week_2          // 第 2 周的挑战题目
```

## 使用步骤
0. 安装好python开发环境与git

1. Fork本项目至自己的github仓库
  * 点击上方的Fork按钮
  * 至此，你自己的仓库中应该有一个叫做pyweek的项目。链接为：https://github.com/yourname/pyweek

2. clone你的项目到本地
  * 打开你的shell，进入你的工作目录，例如： cd ~/workspace/
  * clone项目： git clone https://github.com/yourname/pyweek.git
  * 至此，workspace/pyweek 就有了。

3. 设置上游仓库
  * 先查看远程仓库
      ```
      $ cd ~/workspace/pyweek
      ~/workspace/pyweek $ git remote -v
      origin    https://github.com/yourname/pyweek.git (fetch)
      origin    https://github.com/yourname/pyweek.git (push)
      ```

  * 添加上游远程仓库
      ```
      ~/workspace/pyweek $ git remote add upstream https://github.com/pyweek/pyweek.git
      ```

4. 同步上游master(主干)分支最新代码(每次工作前都应先同步代码，避免较多的冲突)
     ```
     ~/workspace/pyweek $ git pull --rebase upstream master
     ```

5. 添加自己的目录与文件
    ```
    ~/workspace/pyweek $ cd week_1/answers
    ~/workspace/pyweek/week_1/answers $ mkdir yourname
    ~/workspace/pyweek/week_1/answers $ cd yourname
    ~/workspace/pyweek/week_1/answers/yourname $ vim answer.py
    ```

6. 提交代码至自己的仓库
    ```
    $ cd ~/workspace/pyweek
    ~/workspace/pyweek $ git status
    ~/workspace/pyweek $ git add week_1/answers/yourname/
    ~/workspace/pyweek $ git commit -m "基于xx算法的无敌超级答案"   # 注释说明你这次修改做了什么，不要一个词语 update, fix 之类的
    ~/workspace/pyweek $ git pull --rebase upstream master          # 再次与上游同步，也许你工作期间别人已经提交了代码，解决冲突
    ~/workspace/pyweek $ git push origin master                     # 将解决冲突无误后的代码提交至自己远程仓库中的 master 分支, 大项目开发时也许是develop分支，也许是bug-fix分支
    ```

7. 登录github进入自己的项目向上游仓库发起 Pull Request 等待被合并

**注意，一定要养成在开始工作前与提交代码前从上游仓库同步最新代码的习惯**
