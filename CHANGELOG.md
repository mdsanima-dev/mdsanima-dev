# {octicon}`checklist;1em;sd-text-secondary` `CHANGELOG`

All notable changes to this project will be documented in this file.

Please check
[standard-version {octicon}`link-external;0.8em`](https://github.com/conventional-changelog/standard-version)
and documentation for commit guidelines. Also you should check
[conventional-changelog {octicon}`link-external;0.8em`](https://github.com/mdsanima/conventional-changelog)
for more detail.

Docomentation for _Python_ package
[mdsanima-dev {octicon}`link-external;0.8em`](https://pypi.org/project/mdsanima-dev) is available
at [GitHub Pages {octicon}`link-external;0.8em`](https://mdsanima-dev.github.io/mdsanima-dev/)
be sure to check it.

## [0.2.0](https://github.com/mdsanima-dev/mdsanima-dev/compare/v0.1.1...v0.2.0)

_Date:_ _2023-05-12_

{octicon}`alert;1em;sd-text-warning`{bdg-danger-line}`BREAKING CHANGES`

- dynamic version and drop python3.7 python3.8 and python3.9

{octicon}`file-code;1em;sd-text-secondary`{bdg-light-line}`REFACTOR`

- convert images to `webp` format closes [#49](https://github.com/mdsanima-dev/mdsanima-dev/issues/49) ([8e7a13c](https://github.com/mdsanima-dev/mdsanima-dev/commit/8e7a13c1a431d6b8025be0b566fee18ebce834b9))
- dynamic version and drop py3.7 py3.8 py3.9 closes [#48](https://github.com/mdsanima-dev/mdsanima-dev/issues/48) ([5555845](https://github.com/mdsanima-dev/mdsanima-dev/commit/5555845b8d22eee3cdaf97defe7195ade20d1310))
- moved and renamed ([cb0d226](https://github.com/mdsanima-dev/mdsanima-dev/commit/cb0d22622007d02b4926f72e37acb394eff84e7e))

{octicon}`pulse;1em;sd-text-secondary`{bdg-warning-line}`BUG FIXES`

- add `CODEOWNERS` file and adding author ([0e5bfe3](https://github.com/mdsanima-dev/mdsanima-dev/commit/0e5bfe32065358a96a125360b55c68b6c2ed0da9))
- dynamic version from `setuptools_scm` package ([b0d197c](https://github.com/mdsanima-dev/mdsanima-dev/commit/b0d197c517463af1164719a52cab1fd553482aa1))

{octicon}`server;1em;sd-text-secondary`{bdg-primary-line}`BUILD SYSTEM`

- **deps-dev:** bump wheel from 0.37.1 to 0.38.1 in /docs ([ca55d8a](https://github.com/mdsanima-dev/mdsanima-dev/commit/ca55d8aff621bd8d32b0ddada14ee80a31a83d2d))
- dev dependencies ([8f46855](https://github.com/mdsanima-dev/mdsanima-dev/commit/8f46855987e7e11c9e73cecb75d9895770e85e34))
- keep this direcotry ([399ffd0](https://github.com/mdsanima-dev/mdsanima-dev/commit/399ffd04e29b89fa9c75693b969a578f061c44de))
- new config flake8 pylint and max line length closes [#47](https://github.com/mdsanima-dev/mdsanima-dev/issues/47) ([76fc8b6](https://github.com/mdsanima-dev/mdsanima-dev/commit/76fc8b690c24f5e8a74e08242bbc969c16013c2e))
- new config setup ([2bdc17c](https://github.com/mdsanima-dev/mdsanima-dev/commit/2bdc17c2223eedab2fab5e3ddb029d98594a3333))
- pylint ignore ([6f7abb3](https://github.com/mdsanima-dev/mdsanima-dev/commit/6f7abb3bcd7dec5d94760445c7999bb49d411e15))
- sort and remove unnecessary package ([48d9784](https://github.com/mdsanima-dev/mdsanima-dev/commit/48d97840ccdf02a127fada3001676c4fbd3c1d4b))
- update year ([4167e9d](https://github.com/mdsanima-dev/mdsanima-dev/commit/4167e9d987e9c994ded229f4a7f230567d32e665))

{octicon}`book;1em;sd-text-secondary`{bdg-secondary-line}`DOCUMENTATION`

- add image to getting started page ([6f70059](https://github.com/mdsanima-dev/mdsanima-dev/commit/6f70059ee9a709bea84599c9a773c93b994789e0))
- add info for change default branch to `main` on remote repo ([fac5c48](https://github.com/mdsanima-dev/mdsanima-dev/commit/fac5c486030d60a6194809ebfc7617879fdd26c3))
- remove instalation instruction using `setup` and `whell` ([3f78f3a](https://github.com/mdsanima-dev/mdsanima-dev/commit/3f78f3adce604af924d66931706d6ee339674273))

## [0.1.1](https://github.com/mdsanima-dev/mdsanima-dev/compare/v0.1.0...v0.1.1)

_Date:_ _2022-05-02_

{octicon}`pulse;1em;sd-text-secondary`{bdg-warning-line}`BUG FIXES`

- added email address ([bd600ab](https://github.com/mdsanima-dev/mdsanima-dev/commit/bd600ab56c73d70b81e5f8631d512df55f6eaae1))
- **build-system:** add new keywords and classifiers ([90d4cc9](https://github.com/mdsanima-dev/mdsanima-dev/commit/90d4cc9eacfe98ba70bf4115c0f11a8ab2c27e55))
- **build-system:** black format change variable name ([ef5f0b9](https://github.com/mdsanima-dev/mdsanima-dev/commit/ef5f0b9dfd746e077a07126f595078eda145c29a))
- **build-system:** configuration for black python code formatter ([a8100e1](https://github.com/mdsanima-dev/mdsanima-dev/commit/a8100e156eb8e9cbe15e21ce07b946cc59781dfb))
- **build-system:** isort options for sorting import ([4f93078](https://github.com/mdsanima-dev/mdsanima-dev/commit/4f930782b4e19bce1e6af73046ea9d06ef63f3d5))
- **build-system:** sidebar name change brand text size ([c9e1e4f](https://github.com/mdsanima-dev/mdsanima-dev/commit/c9e1e4fbb94731b86fd85377d5cced48ab2ab624))
- **console-scripts:** fix shell script `mdsanima-dev-converts` name ([b10e65f](https://github.com/mdsanima-dev/mdsanima-dev/commit/b10e65fcf4e6565974652b6ed905c2c2f4fda4bf))
- **devs:** black profile formater ([4cfca93](https://github.com/mdsanima-dev/mdsanima-dev/commit/4cfca9320cb0a872f4cfab7b68cb3597b5031e45))
- add json config on `.editorconfig` ([745107c](https://github.com/mdsanima-dev/mdsanima-dev/commit/745107cccb892a8dca3009c25a0b0a6c3b1c01ce))
- added current year to `LICENSE` file ([69eb229](https://github.com/mdsanima-dev/mdsanima-dev/commit/69eb2290dfaa8ca326135be04f6bd94a1a5028bb))

{octicon}`tools;1em;sd-text-secondary`{bdg-danger-line}`TESTS`

- print pacage data from json ([0db5e2e](https://github.com/mdsanima-dev/mdsanima-dev/commit/0db5e2e7862dbb8720d7a877c15b7115eab65d40))
- rename file and fix variable the same on `setyp.py` file ([b16a061](https://github.com/mdsanima-dev/mdsanima-dev/commit/b16a0615af82de90f122983673070a804c96a579))
- variable the same on `setyp.py` file ([f52a40d](https://github.com/mdsanima-dev/mdsanima-dev/commit/f52a40d5fec9f76670e838df9bf994817d98a5b3))

{octicon}`telescope;1em;sd-text-secondary`{bdg-success-line}`FEATURES`

- **console-script:** add entry points to `setup.py` console script ([e02ed84](https://github.com/mdsanima-dev/mdsanima-dev/commit/e02ed84c038725516c7a75c7b58418bdc0a8fca5)), closes [#19](https://github.com/mdsanima-dev/mdsanima-dev/issues/19) [#20](https://github.com/mdsanima-dev/mdsanima-dev/issues/20)
- **convert:** converts frames to time code formats closes [#14](https://github.com/mdsanima-dev/mdsanima-dev/issues/14) ([4a10533](https://github.com/mdsanima-dev/mdsanima-dev/commit/4a1053386029923359a942d61872465abff7df96))
- **converts:** time code `00:00:00:00` formats to frames closes [#18](https://github.com/mdsanima-dev/mdsanima-dev/issues/18) ([abd260b](https://github.com/mdsanima-dev/mdsanima-dev/commit/abd260bde1db066dc9430784bc2a1a599e76d45a)), closes [#14](https://github.com/mdsanima-dev/mdsanima-dev/issues/14)
- **docs:** add quick tutorials articles ([4666e88](https://github.com/mdsanima-dev/mdsanima-dev/commit/4666e88c2df34239e0fccde4a9147264a80faa6d))

{octicon}`book;1em;sd-text-secondary`{bdg-secondary-line}`DOCUMENTATION`

- open graph metadata sphinx extension ([74a42bf](https://github.com/mdsanima-dev/mdsanima-dev/commit/74a42bf300fcf45b5d9977c9a59e6d9c8901ac52))
- project information badge links and theme ([fe1d693](https://github.com/mdsanima-dev/mdsanima-dev/commit/fe1d693d32a34c50c4860bf3ff74ab0021f4e52c))
- quick tutorial how to rename local and remote git branch ([efef3d4](https://github.com/mdsanima-dev/mdsanima-dev/commit/efef3d465c59c951c29136c10061131e688b8362))
- **gif:** remove unused gif ([eae4468](https://github.com/mdsanima-dev/mdsanima-dev/commit/eae4468c90b2ecf4f6ee7c6c7521d986dba9a2bd))
- **gif:** renamed files ([9418366](https://github.com/mdsanima-dev/mdsanima-dev/commit/9418366ed6de6944b2086f0eaa2c94498d256879))
- **images:** added images for social promo ([dc3439e](https://github.com/mdsanima-dev/mdsanima-dev/commit/dc3439e2f6a53f2b2c1808a77fc1305c9377f397))
- **images:** change image size ([5ac2b92](https://github.com/mdsanima-dev/mdsanima-dev/commit/5ac2b92eb8957239348eaeadefadb70c9d3a7614))
- **images:** delete unused files ([660daac](https://github.com/mdsanima-dev/mdsanima-dev/commit/660daace454fa6987a7b147ea7c4f90d36bd4d9d))
- **images:** reduced one pixel on each side ([8075e43](https://github.com/mdsanima-dev/mdsanima-dev/commit/8075e43afe09ec130cf5090396afdbff5f2065cc))
- **images:** resize images ([67845d6](https://github.com/mdsanima-dev/mdsanima-dev/commit/67845d660badad036df7cec76711abd1f7ed96f9))
- **js:** swap logo and favicon object method color options ([9ff13ba](https://github.com/mdsanima-dev/mdsanima-dev/commit/9ff13ba3b040c48421074e41bdd8b91f800e4f6f))
- **style:** change icon color when active and click animation ([36a668e](https://github.com/mdsanima-dev/mdsanima-dev/commit/36a668edd7ca0b79fec6ebee46b0c94d0e0c56ae))
- **style:** color card bg and align and resize gif on home page ([938149d](https://github.com/mdsanima-dev/mdsanima-dev/commit/938149d6351b20752a5ca0b2df70b81b626cebb3))
- **style:** custom code block colors ([cbc2c73](https://github.com/mdsanima-dev/mdsanima-dev/commit/cbc2c73172322dcce9436941588cfbfa43bce213))
- **style:** fix bacground code literal ([d666587](https://github.com/mdsanima-dev/mdsanima-dev/commit/d66658770200c92474da9bd6288f9c904d2bd2bd))
- **theme:** color border on code block markdown ([093ea6e](https://github.com/mdsanima-dev/mdsanima-dev/commit/093ea6e9a4277296ba1a9d950c2a550a310a2948))
- add `svg` logo mdsanima default with 27 colors options ([7c3fbd5](https://github.com/mdsanima-dev/mdsanima-dev/commit/7c3fbd53bca70cc73436b01f4afa034da5d0c668))
- add color badge and fix tab item path ([aaaa37a](https://github.com/mdsanima-dev/mdsanima-dev/commit/aaaa37a6d4b1d5a2ab4d87addb2ebc82d6605cd6))
- add png logo and docstring fixes ([91b25e8](https://github.com/mdsanima-dev/mdsanima-dev/commit/91b25e82d371db5fc2c8e347d8842d89c4fa275f))
- added examples code show on gif ([72d4949](https://github.com/mdsanima-dev/mdsanima-dev/commit/72d49493568c28ce17e3f06e5d1292a251e91fff))
- addin new links and badge layouts closes [#16](https://github.com/mdsanima-dev/mdsanima-dev/issues/16) ([28a39db](https://github.com/mdsanima-dev/mdsanima-dev/commit/28a39dbe07bb0f30a138b36589caf1ae3a9a28a6)), closes [#17](https://github.com/mdsanima-dev/mdsanima-dev/issues/17)
- change badge color ([acc3f59](https://github.com/mdsanima-dev/mdsanima-dev/commit/acc3f59fba0b2aec66388518b67723e73f222c4f))
- custom css furo theme ([866c19c](https://github.com/mdsanima-dev/mdsanima-dev/commit/866c19c142e944852dc68a4e720ba89be07686e3))
- docstring cleanup ([e15a31e](https://github.com/mdsanima-dev/mdsanima-dev/commit/e15a31ef4bc9c69cf395ceb1c2fe62b849cade61))
- fix custom css file ([7fbab62](https://github.com/mdsanima-dev/mdsanima-dev/commit/7fbab62e3b745fb4fa9e4db449845960fe622ff7))
- fix directives ([7ff618b](https://github.com/mdsanima-dev/mdsanima-dev/commit/7ff618b21c60b385edd30b3cb3c639cf57050016))
- fix docstring ([2507345](https://github.com/mdsanima-dev/mdsanima-dev/commit/25073458c379310c5f8f1726b5eb2185a4c5baf8))
- fix docstring ([53beba5](https://github.com/mdsanima-dev/mdsanima-dev/commit/53beba5e6a176c1f5f04ae71c9676b8aaffb94d3))
- fix docstring ([df1290c](https://github.com/mdsanima-dev/mdsanima-dev/commit/df1290c4f5cca41fe5701add8e7dcb17b9fb1d6e))
- fix docstring ([656615f](https://github.com/mdsanima-dev/mdsanima-dev/commit/656615ff28dce96f2fb8181d3f7d1db7df6f436d))
- fix docstring ([ae4b5af](https://github.com/mdsanima-dev/mdsanima-dev/commit/ae4b5af21584d22939df7f2be2c84615415b14a8))
- fix docstring and image path ([f19f731](https://github.com/mdsanima-dev/mdsanima-dev/commit/f19f731a5d3e72370391871b3a6e0a041a736a31))
- fix docstring for sphinx build ([b63de3f](https://github.com/mdsanima-dev/mdsanima-dev/commit/b63de3f63a9f7eb8324649f62af171133a44b98c))
- fix docstring links path and badge color ([4503dab](https://github.com/mdsanima-dev/mdsanima-dev/commit/4503dab0ef274e327f72c7e00df1001b992b817f))
- fix include path ([75abb83](https://github.com/mdsanima-dev/mdsanima-dev/commit/75abb83531848512ce7b0bcbe7ffa3d0975509aa))
- fix information and toctree ([85d2a3f](https://github.com/mdsanima-dev/mdsanima-dev/commit/85d2a3f4d70d6aa2b9aa916d3d5325c1104d47fd))
- fix link adn build development help ([661838c](https://github.com/mdsanima-dev/mdsanima-dev/commit/661838cce2b1a38e1593b65c6023111edadf257f))
- fix logo and favicon ([e42fe5c](https://github.com/mdsanima-dev/mdsanima-dev/commit/e42fe5ca7a89da092f1add8fd073cd21ceaa2c88))
- fix some docstring and isort import ([d10247d](https://github.com/mdsanima-dev/mdsanima-dev/commit/d10247d6193d3e373e7a679b0080fe41ff90167c))
- fix some docstring and remove unnesesery lines ([28cae88](https://github.com/mdsanima-dev/mdsanima-dev/commit/28cae8899451ae063090fbef03edd0a35d4715cc))
- fix some docstring and rename and move files ([be1eaeb](https://github.com/mdsanima-dev/mdsanima-dev/commit/be1eaeb2446a9997e3d1946b3efb6d539cbf38ec))
- fix some docstring reorder function position and move files ([1666026](https://github.com/mdsanima-dev/mdsanima-dev/commit/16660263a43ef70c0a251f2b9913a0a36a96933b))
- fixing documentation string ([d5fb5ff](https://github.com/mdsanima-dev/mdsanima-dev/commit/d5fb5ff4f5ccd865bbc30045689905a89ae9d8de))
- fixing theme colors tabs overline underline api name ([4eb5929](https://github.com/mdsanima-dev/mdsanima-dev/commit/4eb59295b4b52a6126db4b3ec46236720d73297f))
- font awesome css file ([c914fd2](https://github.com/mdsanima-dev/mdsanima-dev/commit/c914fd2c75ffcbaf91cfe0e1b5ceaee298047902))
- getting started installation info help ([cba3381](https://github.com/mdsanima-dev/mdsanima-dev/commit/cba338185a474367110704fe70f8413f0439dfe3))
- logo and favicon svg ([b8046b7](https://github.com/mdsanima-dev/mdsanima-dev/commit/b8046b797eaed4b45b41e2f7c06cde25a7e54d48))
- moved image to new folder ([9c39c4f](https://github.com/mdsanima-dev/mdsanima-dev/commit/9c39c4f42b2f43420ddfcfa3c1298fcee311d293))
- moved in to folder ([46720ef](https://github.com/mdsanima-dev/mdsanima-dev/commit/46720efa14d499e26644184d75d4df4fd683bfce))
- path to html `js` files on config and blank `.js` file ([e643663](https://github.com/mdsanima-dev/mdsanima-dev/commit/e6436632c7f634a3dcb29f2ca0366d275d70dc80))
- remove options ([cc8bf4f](https://github.com/mdsanima-dev/mdsanima-dev/commit/cc8bf4ff0884ecc551bb833493a2736c23450d03))
- rename and move file ([188fbd6](https://github.com/mdsanima-dev/mdsanima-dev/commit/188fbd6cc43d32cb4d5d78dabd3b0fb4938cfde4))
- space between caption elements and fix docstring ([942da17](https://github.com/mdsanima-dev/mdsanima-dev/commit/942da179d7c076627b132b1111bb8d9ecda35194))
- **console-script:** sphinx documentation for `console scripts` option ([165671a](https://github.com/mdsanima-dev/mdsanima-dev/commit/165671a06c6f7bf10b7f69ff55f2e2749ddac70c))
- **devs:** clean code and fix some docstring ([27fcd3c](https://github.com/mdsanima-dev/mdsanima-dev/commit/27fcd3cc4479a757f596051d210f8d87b6633476))
- **devs:** extra require docs and fix some string ([d7fcc06](https://github.com/mdsanima-dev/mdsanima-dev/commit/d7fcc062644d76aed359a47f71a41177ba401d53))

## 0.1.0

_Date:_ _2021-08-13_

{octicon}`telescope;1em;sd-text-secondary`{bdg-success-line}`FEATURES`

- **build-system:** template file to help building `mdsanima-dev` python package ([6839cab](https://github.com/mdsanima-dev/mdsanima-dev/commit/6839cab06a55b1a3e04831b361d50daa293e35a6))
- **build-system:** this file is the build script for setuptools ([54f990e](https://github.com/mdsanima-dev/mdsanima-dev/commit/54f990e0117648be830bc18ecf1ac97c7128028d))
- **colors:** add color number show options `False` or `True` ([6670265](https://github.com/mdsanima-dev/mdsanima-dev/commit/6670265db59900e048cc90435f897852c0931ab5))
- **colors:** add function `get_complex_color` colored text in console ([7a6704c](https://github.com/mdsanima-dev/mdsanima-dev/commit/7a6704c350116595976a50f8091c7fa60ad2f27e))
- **colors:** function `get_complex_color` works the same like print ([76fab2b](https://github.com/mdsanima-dev/mdsanima-dev/commit/76fab2ba7fd348096b5e36065e575c01542d3366))
- **devs:** workflow bumping version in `__init__.py` file closes [#1](https://github.com/mdsanima-dev/mdsanima-dev/issues/1) ([d38babd](https://github.com/mdsanima-dev/mdsanima-dev/commit/d38babdeb405d4d4cd3d214a3dfe5a092b1799d8))
- **emoji:** add two class for show entire collection of emoji ([0ae038e](https://github.com/mdsanima-dev/mdsanima-dev/commit/0ae038e751534bd7dc226472af863929d0d9fc4f))
- **emoji:** request data from url and store clean json dictionary ([bfa0a94](https://github.com/mdsanima-dev/mdsanima-dev/commit/bfa0a946d0dfec09c079d255e46d43a44cc338a8))
- **standard-version:** automate versioning and changelog generation ([8ede8db](https://github.com/mdsanima-dev/mdsanima-dev/commit/8ede8db885e42372ffb22e482df988a0130479d5))
- **table:** making a cool table what you wnat ([3d28efe](https://github.com/mdsanima-dev/mdsanima-dev/commit/3d28efeb998922dd20e056623d4ae210ce7e7004))
- **tools:** useful functions that I usually use fro python coding ([20439f5](https://github.com/mdsanima-dev/mdsanima-dev/commit/20439f55c4f621502d9e46459085f51f7793d596))
- add function `show_complex_color` prints all avaiable colors ([437969a](https://github.com/mdsanima-dev/mdsanima-dev/commit/437969a61bc6a0d5f0093c061cc1a0064bd499a1))
- initial python file required to import the directory as a package ([cfefad5](https://github.com/mdsanima-dev/mdsanima-dev/commit/cfefad56a43d09d6e7f73972fa2e060576c0c7e7))

{octicon}`pulse;1em;sd-text-secondary`{bdg-warning-line}`BUG FIXES`

- double parenthesis instead of single `__version__` ([38eb1ac](https://github.com/mdsanima-dev/mdsanima-dev/commit/38eb1ac331e0987b1dca985c1bf6a8eb981fd6e7))
- **build-system:** fix documentation url `github-pages` ([0e00e36](https://github.com/mdsanima-dev/mdsanima-dev/commit/0e00e360e6182c40d0671c410f6f345fe710a5d7))
- **build-system:** pacage name and dev dependencies ([1b7f25f](https://github.com/mdsanima-dev/mdsanima-dev/commit/1b7f25feddc0686e37323937f00c240c79d8cc9e))
- **build-system:** requires version of setuptools and clean code ([c11f0d0](https://github.com/mdsanima-dev/mdsanima-dev/commit/c11f0d0b20b41fcfffc428e450b528d61faa591c))
- **colors:** function `get_complex_color` now return string ([ab24e34](https://github.com/mdsanima-dev/mdsanima-dev/commit/ab24e342cec079bb8745dc724e92f53e16bf0cb0))
- **docs:** build directory for `sphinx` html ([13736c0](https://github.com/mdsanima-dev/mdsanima-dev/commit/13736c0f7d8918fda7dbc5412cad5e0f5dbb84e0))
- add name to `LICENSE` file ([3258000](https://github.com/mdsanima-dev/mdsanima-dev/commit/3258000bd33bf6270e42be9cd423bcccdf8d126d))
- new script `npm` and data pacage on `setup.py` file ([db246ae](https://github.com/mdsanima-dev/mdsanima-dev/commit/db246aecb639665743234904e209e526c63756d8))
- **emoji:** end of string parameter ([9ef92e0](https://github.com/mdsanima-dev/mdsanima-dev/commit/9ef92e075712dd33995f9693a54b0208ce23d4ee))
- **progress:** remove end string on progress bar ([4abf6df](https://github.com/mdsanima-dev/mdsanima-dev/commit/4abf6df0cf88cb34dceed0254acc440042871012))
- add spaces on function arguments ([b45720c](https://github.com/mdsanima-dev/mdsanima-dev/commit/b45720ce4adde3a2bebb75538db43b9e4da738cf))
- readme template ([5f3ed98](https://github.com/mdsanima-dev/mdsanima-dev/commit/5f3ed982a3320489e7c1148f83abdfc5c1273ec9))
- **colors:** now info **show complex** printing with colors ([2dd0c13](https://github.com/mdsanima-dev/mdsanima-dev/commit/2dd0c138a298a004dbd818a7f2184e8eb0db22b0))
- **emoji:** for installable python apps in develompment ([191018b](https://github.com/mdsanima-dev/mdsanima-dev/commit/191018b3b3c4ded9dd26829cdfb040067c73babf))
- **emoji:** removed unnecessary comment ([b828e6b](https://github.com/mdsanima-dev/mdsanima-dev/commit/b828e6ba8f8c5d5569a091f831a2fee8394c236d))
- add `__version__` variable ([1d1bd60](https://github.com/mdsanima-dev/mdsanima-dev/commit/1d1bd608ad73363ebf98c97cc2511db9869417c7))
- initial **README** `mdsanima-dev` python package ([a92a067](https://github.com/mdsanima-dev/mdsanima-dev/commit/a92a0676d5b98d54218aed636f47f1ff21e0060d))
- template file helps consistent clean coding style ([2118ae2](https://github.com/mdsanima-dev/mdsanima-dev/commit/2118ae228ac517a1d9c406346b45dd69e8a2478b))

{octicon}`tools;1em;sd-text-secondary`{bdg-danger-line}`TESTS`

- printing data from `package.json` file to check if working ([5359db7](https://github.com/mdsanima-dev/mdsanima-dev/commit/5359db722d2b44754701b7f4a490297e4ce6287e))

{octicon}`book;1em;sd-text-secondary`{bdg-secondary-line}`DOCUMENTATION`

- fix badge and some docstring ([16a27d6](https://github.com/mdsanima-dev/mdsanima-dev/commit/16a27d64c1be1cb58d651a16a14b293572db0d3f))
- **devs:** development instruction workflow ([7dfec4c](https://github.com/mdsanima-dev/mdsanima-dev/commit/7dfec4c72584f4d907df500cbc70a8514733199c))
- **gh-pages:** build setup fixed ([29a63e0](https://github.com/mdsanima-dev/mdsanima-dev/commit/29a63e088e48d0f5b492c0c5c846a4969eb8ae4f))
- add `toctree` changelog for `sphinx` documentation ([4aae253](https://github.com/mdsanima-dev/mdsanima-dev/commit/4aae2533f6edcae573baea5bb5cf82a24407cdf3))
- add badge to `README.md` file ([6ee2d6b](https://github.com/mdsanima-dev/mdsanima-dev/commit/6ee2d6b4a85852db6b3bd72c9dc921840dc54853))
- add documentation string ([7faf2b0](https://github.com/mdsanima-dev/mdsanima-dev/commit/7faf2b0213e8971fb073a6daac9f490cd0740f27))
- fix package name on `pypi` install ([bde85ef](https://github.com/mdsanima-dev/mdsanima-dev/commit/bde85ef73eb821f24ddf0b3d37551719b97b73f8))
- **gh-pages:** fix redirecting `url` ([7643624](https://github.com/mdsanima-dev/mdsanima-dev/commit/7643624cfcab90e63981b3795813b87217bd661a))
- fix duplicate label ([2c2ed8a](https://github.com/mdsanima-dev/mdsanima-dev/commit/2c2ed8aaeb91177452391adf5c36e7ef3ea2fbc2))
- **fix:** repository clone url ([bee45c7](https://github.com/mdsanima-dev/mdsanima-dev/commit/bee45c726c14a68eb4b09e745e28836980c98314))
- **gh-pages:** create empty `.nojekyll` closes [#12](https://github.com/mdsanima-dev/mdsanima-dev/issues/12) ([5bb21b2](https://github.com/mdsanima-dev/mdsanima-dev/commit/5bb21b201c89951d794d88b2f4eb865f8b815ee0))
- **gh-pages:** meta `url` refers `index.html` closes [#11](https://github.com/mdsanima-dev/mdsanima-dev/issues/11) ([c4ceac7](https://github.com/mdsanima-dev/mdsanima-dev/commit/c4ceac7fdd3f5eeb64a42389d773f3ae3110149e))
- **gh-pages:** meta contents refers to `build` shpinx closes [#13](https://github.com/mdsanima-dev/mdsanima-dev/issues/13) ([5545f4a](https://github.com/mdsanima-dev/mdsanima-dev/commit/5545f4a5618b4ab955679ffb13743ed70594bf0d))
- **gif:** add gif animation closes [#10](https://github.com/mdsanima-dev/mdsanima-dev/issues/10) ([de8e9ca](https://github.com/mdsanima-dev/mdsanima-dev/commit/de8e9caa4fce235f21d2f3a2c58b13bcd94155a1)), closes [#2](https://github.com/mdsanima-dev/mdsanima-dev/issues/2)
- add `extension` and `markdown` parser closes [#3](https://github.com/mdsanima-dev/mdsanima-dev/issues/3) ([38b3552](https://github.com/mdsanima-dev/mdsanima-dev/commit/38b3552116817fce65fc1e6b45587e43a9e5faea))
- add `README.md` information ([2efd757](https://github.com/mdsanima-dev/mdsanima-dev/commit/2efd7574848e5f09b013f2efc98427a21b72d42d))
- add theme and html option closes [#4](https://github.com/mdsanima-dev/mdsanima-dev/issues/4) ([765ed8e](https://github.com/mdsanima-dev/mdsanima-dev/commit/765ed8e6b8c57e1118428737c6f78cc0ac60089b))
- deteting old files `.rst` and make ([778eee6](https://github.com/mdsanima-dev/mdsanima-dev/commit/778eee6a88c60f21a11a79127e4efdc0e958f6f5))
- sphinx documentation `colors` module closes [#6](https://github.com/mdsanima-dev/mdsanima-dev/issues/6) ([5ff370f](https://github.com/mdsanima-dev/mdsanima-dev/commit/5ff370f66112987f544856b54a1a91bd2469af80))
- sphinx documentation `emoji` module closes [#7](https://github.com/mdsanima-dev/mdsanima-dev/issues/7) ([7271791](https://github.com/mdsanima-dev/mdsanima-dev/commit/727179192d844a744aeb0aac42f0f2ece05d27e8))
- sphinx documentation `table` module closes [#8](https://github.com/mdsanima-dev/mdsanima-dev/issues/8) ([c744291](https://github.com/mdsanima-dev/mdsanima-dev/commit/c74429171e74bdc223fbc6a405f0c3597d313b44))
- sphinx documentation `tools` module closes [#9](https://github.com/mdsanima-dev/mdsanima-dev/issues/9) ([65a3a65](https://github.com/mdsanima-dev/mdsanima-dev/commit/65a3a65c73e8b7655545a8200c11eedfb7562a63))
- sphinx documentation main `index.md` files closes [#5](https://github.com/mdsanima-dev/mdsanima-dev/issues/5) ([d8eb0f1](https://github.com/mdsanima-dev/mdsanima-dev/commit/d8eb0f16c07293cb52d2438d7d8e9713ae554e90))
- **build-system:** auto generate `sphinx` python documentation ([fbbe045](https://github.com/mdsanima-dev/mdsanima-dev/commit/fbbe045e01dc0a39f3d3baa12d0bd3ca6082b1b7))
- **colors:** documentation colors string ([d325764](https://github.com/mdsanima-dev/mdsanima-dev/commit/d32576405c5d87234f60be3ad749444996b0b23f))
- **emoji:** add documentation string to a function ([86c6037](https://github.com/mdsanima-dev/mdsanima-dev/commit/86c6037ca6db19b7b7ba5621c23f29befdd5fea6))
- **emoji:** documentation emoji string ([4853b78](https://github.com/mdsanima-dev/mdsanima-dev/commit/4853b788e5710d1ce965229f60342be0fb0dc00a))
- **gif:** add gif animation showcase ([b5c26e0](https://github.com/mdsanima-dev/mdsanima-dev/commit/b5c26e09250f977712488e8a7d88ef05f508fa39))
- **icons:** add `mdsanima` icons logos variation ([7ac931a](https://github.com/mdsanima-dev/mdsanima-dev/commit/7ac931a6ac81f3b4bde45e4d9dfefc1056048bb0))
- **screenshot:** add console screenshot img ([762bdc8](https://github.com/mdsanima-dev/mdsanima-dev/commit/762bdc838b6776970fad0ebc028e4ece8c841990))
- **table:** add docstring for `sphinx` documentation ([bcb3028](https://github.com/mdsanima-dev/mdsanima-dev/commit/bcb302840b5609974dc3c7708016b8c0b4b2f3d9))
- **test:** add screenshot test img ([e77204b](https://github.com/mdsanima-dev/mdsanima-dev/commit/e77204b59065df1480c7fbe5761917daa8dfe0f0))
- **tools:** add docstring for `sphinx` documentation ([7b0ac87](https://github.com/mdsanima-dev/mdsanima-dev/commit/7b0ac87fea5ccee06c4f2177844587b1294036b4))
- template configuration file shuld be changed ([3c7080f](https://github.com/mdsanima-dev/mdsanima-dev/commit/3c7080fb64a72a55dbe7f18b4094e255b1cbd4ef))
