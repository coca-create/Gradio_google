## 1. アプリケーションライセンス (PeriOz web v1.0)

- このソフトウェアのすべての権利は著作権者が保有します。

- 使用条件：
  本ソフトウェアの使用は、以下の条件に同意した場合にのみ許可されます。

  - 個人使用に限定：
   本ソフトウェアは、個人的および非商業的な目的に限り使用することができます。商業的な使用は、著作権者の事前の書面による許可が必要です。

  - 二次配布の禁止：
    本ソフトウェアの全部または一部を、いかなる形式でも再配布することは禁止されています。これには、改変を含む場合でも含まない場合でも、他のソフトウェアやパッケージに組み込むことや、インターネット上での共有が含まれます。

  - 改変の禁止：
   本ソフトウェアのソースコードの改変、リバースエンジニアリング、逆アセンブル、逆コンパイル、またはその他の手段による解析は禁止されています。

  - 譲渡の禁止：
   本ソフトウェアの使用権は譲渡できません。他者に貸与、譲渡、サブライセンスすることはできません。

  - 著作権表示の保持：
    本ソフトウェアのすべてのコピーには、この著作権表示および使用条件を含めなければなりません。

- 免責条項：
  本ソフトウェアは「現状のまま」で提供されます。著作権者は、本ソフトウェアに関していかなる明示的または黙示的な保証も行いません。これには、特定の目的への適合性や商品性の黙示的な保証が含まれますが、これに限られません。法律が許容する最大限の範囲で、著作権者は、本ソフトウェアの使用または使用不能によって発生するいかなる損害に対しても責任を負いません。これには、データの損失、収益の喪失、業務の中断、またはその他の商業的損害が含まれますが、これに限られません。

<br>

## 2. Third Party LICENSES

  このアプリケーションは、以下のサードパーティのライブラリを利用しています。各ライブラリの詳細なライセンス情報は、ルートディレクトリ内の`Third Party License Documents`フォルダに同梱されたファイルを参照してください。また、これらのライブラリを使用する際には、それぞれのライセンス条件に従う必要がありますので、インストール前に必ず確認し、同意の上でインストール、ご利用ください。
<br>  

### 2-1. PYTHON,FFMPEGとライセンス
- PYTHON

  - version 3.11.8

  - [Download link](https://www.python.org/downloads/release/python-3118/)
  - [History and License](https://docs.python.org/3.11/license.html)

- FFMPEG v7.0.2

  - ffmpeg-n7.0.2-win64-lgpl-7.0.zipをダウンロード,解凍後に同梱しています。アプリケーションのルートディレクトリのbinフォルダに配置してあります。-  - [Downlod Link](https://github.com/BtbN/FFmpeg-Builds/releases)
  - FFMPEG ライブラリは、LGPL ライセンスに準拠しており、改変せずにアプリケーション内で使用しています。ライセンス文は[Github](https://github.com/FFmpeg/FFmpeg/blob/master/LICENSE.md)で確認できます。また、Third Party License Documentsにも同梱してありますので、ご確認ください。

<br>

### 2-2. NVIDIA CUDAおよびcuDNNに関するライセンス

  本アプリケーションには、NVIDIA Corporation の CUDA Toolkit および cuDNN ランタイムコンポーネントが含まれています。これらのコンポーネントは、以下のライセンス条件に基づいて再配布されています。

<br>

#### 2-2-1. NVIDIA CUDA Toolkit (再配布可能なランタイムコンポーネント)
以下のファイルは、NVIDIA CUDA EULAの条件に基づき再配布が許可されています：

- `cublas64_12.dll`
- `cublasLt64_12.dll`
- `cudart64_12.dll`

詳しいライセンス情報については、以下を参照してください：
[NVIDIA CUDA EULA](https://docs.nvidia.com/cuda/eula/index.html)

<br>

#### 2-2-2. NVIDIA cuDNN

  以下のファイルは、NVIDIA cuDNN Software License Agreementの条件に基づき再配布が許可されています：

- `cudnn_cnn_infer64_8.dll`
- `cudnn_cnn64_9.dll`
- `cudnn_ops_infer64_8.dll`
- `cudnn_ops64_9.dll`
- `cudnn64_8.dll`
- `cudnn64_9.dll`

詳しいライセンス情報については、以下を参照してください：
[NVIDIA cuDNN Software License Agreement](https://docs.nvidia.com/deeplearning/cudnn/latest/reference/eula.html)

<br>

### 2-3.同梱されているpythonにインストール済みのライブラリとライセンス概要

| Name                | Version      | License              | URL                                                              |
|---------------------|--------------|----------------------|------------------------------------------------------------------|
| Jinja2              | 3.1.5        | BSD License          | [Github](https://github.com/pallets/jinja/)                      |
| MarkupSafe          | 2.1.5        | BSD License          | [HP](https://palletsprojects.com/p/markupsafe/)                  |
| PyYAML              | 6.0.2        | MIT License          | [HP](https://pyyaml.org/)                                        |
| Pygments            | 2.18.0       | BSD License          | [HP](https://pygments.org)                                       |
| aiofiles            | 23.2.1       | Apache Software License  | [Github](https://github.com/Tinche/aiofiles)                 |
| annotated-types     | 0.7.0        | MIT License          | [Github](https://github.com/annotated-types/annotated-types)     |
| anyio               | 4.7.0        | MIT License          | [HP](https://anyio.readthedocs.io/en/stable/versionhistory.html) |
| av                  | 14.0.1       | BSD License          | [Github](https://github.com/PyAV-Org/PyAV)                       |
| catalogue           | 2.0.10       | MIT License          | [Github](https://github.com/explosion/catalogue)            |   
| certifi             | 2024.12.14    | Mozilla Public License 2.0 (MPL 2.0) | [Github](https://github.com/certifi/python-certifi)|
| charset-normalizer  | 3.4.1        | MIT License          | [Github](https://github.com/Ousret/charset_normalizer)           |
| click               | 8.1.8        | BSD License          | [HP](https://palletsprojects.com/p/click/)                       |
| cloudpathlib                | 0.20.0      | MIT License   | [Github](https://github.com/drivendataorg/cloudpathlib)                        |
| colorama            | 0.4.6        | BSD License          | [Github](https://github.com/tartley/colorama)                    |
| coloredlogs         | 15.0.1       | MIT License          | [HP](https://coloredlogs.readthedocs.io)                         |
| confection                  | 0.1.5       | MIT License    | [Github](https://github.com/explosion/confection)                              |
| contourpy           | 1.3.0        | BSD License          | [Github](https://github.com/contourpy/contourpy)                 |
| ctranslate2         | 4.4.0        | MIT License          | [HP](https://opennmt.net)                                        |
| curated-tokenizers          | 0.0.9       | MIT License        |[Github](https://github.com/explosion/curated-tokenizers)                      |
| curated-transformers        | 0.1.1       | MIT            | [Github](https://github.com/explosion/curated-transformers)                    |
| cymem                       | 2.0.10      | MIT License    | [Github](https://github.com/explosion/cymem)                                   |
| deepmultilingualpunctuation | 1.0.1       | MIT License    | [Github](https://github.com/oliverguhr/deepmultilingualpunctuation)            |
| en_core_web_trf             | 3.8.0       | MIT        | [HP](https://explosion.ai)                                                 |
| cycler              | 0.12.1       | BSD License          | [HP](https://matplotlib.org/cycler/)                             |
| et-xmlfile          | 2.0.0        | MIT License          | [HP](https://foss.heptapod.net/openpyxl/et_xmlfile)              |
| fastapi             | 0.115.6      | MIT License          | [Github](https://github.com/fastapi/fastapi)                     |
| faster-whisper      | 1.1.0        | MIT License          | [Github](https://github.com/SYSTRAN/faster-whisper)              |
| ffmpy               | 0.5.0        | MIT License          | [Github](https://github.com/Ch00k/ffmpy)                         |
| ffmpeg-python               | 0.2.0       | Apache Software License    | [Github](https://github.com/kkroening/ffmpeg-python)                           |
| filelock            | 3.16.1       | The Unlicense (Unlicense) | [Github](https://github.com/tox-dev/py-filelock)            |
| flatbuffers         | 24.12.23      | Apache Software License  | [HP](https://google.github.io/flatbuffers/)                  |
| fonttools           | 4.54.1       | MIT License          | [Github](http://github.com/fonttools/fonttools)                  |
| fsspec              | 2024.9.0     | BSD License          | [Github](https://github.com/fsspec/filesystem_spec)              |
| future                      | 1.0.0       | MIT License                                       | [Github](https://python-future.org)                                            |
| gradio              | 5.8.0       | Apache Software License | [Github](https://github.com/gradio-app/gradio)                |
| gradio_client       | 1.5.1        | Apache Software License | [Github](https://github.com/gradio-app/gradio)                |
| h11                 | 0.14.0       | MIT License          | [Github](https://github.com/python-hyper/h11)                    |
| httpcore            | 1.0.7        | BSD License          | [HP](https://www.encode.io/httpcore/)                            |
| httpx               | 0.28.1       | BSD License          | [Github](https://github.com/encode/httpx)                        |
| huggingface-hub     | 0.27.0       | Apache Software License | [Github](https://github.com/huggingface/huggingface_hub)      |
| humanfriendly       | 10.0         | MIT License          | [HP](https://humanfriendly.readthedocs.io)                       |
| idna                | 3.10         | BSD License          | [Github](https://github.com/kjd/idna)                            |
| importlib_resources | 6.4.5        | Apache Software License | [Github](https://github.com/python/importlib_resources)       |
| langcodes                   | 3.5.0       | MIT License          | [Github](https://github.com/georgkrause/langcodes)                             |
| language_data               | 1.3.0       | MIT License        | [Github](https://github.com/georgkrause/language_data)                         |
| kiwisolver          | 1.4.7        | BSD License          | [Github](https://github.com/nucleic/kiwi)                        |
| lxml                | 5.3.0        | BSD License          | [HP](https://lxml.de/)                                           |
| markdown-it-py      | 3.0.0        | MIT License          | [Github](https://github.com/executablebooks/markdown-it-py)      |
| marisa-trie                 | 1.2.1       | MIT License      | [Github](https://github.com/pytries/marisa-trie)                               |
| markdown2           | 2.5.1        | MIT License          | [Github](https://github.com/trentm/python-markdown2)             |
| matplotlib          | 3.9.2        | Python Software Foundation License | [HP](https://matplotlib.org)                       |
| mdurl               | 0.1.2        | MIT License          | [Github](https://github.com/executablebooks/mdurl)               |
| mpmath              | 1.3.0        | BSD License          | [HP](http://mpmath.org/)                                         |
| murmurhash                  | 1.0.11      | MIT License                                       | [Github](https://github.com/explosion/murmurhash)                              |
| networkx            | 3.2.1        | BSD License          | [HP](https://networkx.org/)                                      |
| numpy               | 1.26.4        | BSD License          | [HP](https://numpy.org)                                          |
| onnxruntime         | 1.20.1       | MIT License          | [HP](https://onnxruntime.ai)                                     |
| openpyxl            | 3.1.5        | MIT License          | [HP](https://openpyxl.readthedocs.io)                            |
| orjson              | 3.10.12       | Apache Software License; MIT License | [Github](https://github.com/ijl/orjson)          |
| packaging           | 24.2         | Apache Software License; BSD License | [Github](https://github.com/pypa/packaging)      |
| pandas              | 2.2.3        | BSD License          | [HP](https://pandas.pydata.org)                                  |
| pillow              | 11.0.0       | Historical Permission Notice and Disclaimer (HPND) | [HP](https://python-pillow.org)    |
| preshed                     | 3.0.9       | MIT License                                       |[Github](https://github.com/explosion/preshed)                                 |
| protobuf            | 5.29.2       | 3-Clause BSD License | [HP](https://developers.google.com/protocol-buffers/)            |
| pydantic            | 2.10.4        | MIT License          | [Github](https://github.com/pydantic/pydantic)                   |
| pydantic_core       | 2.27.2       | MIT License          | [Github](https://github.com/pydantic/pydantic-core)              |
| pydub               | 0.25.1       | MIT License          | [HP](http://pydub.com)                                           |
| pyparsing           | 3.1.4        | MIT License          | [Github](https://github.com/pyparsing/pyparsing/)                |
| pyreadline3         | 3.5.4        | BSD License          | [Github](https://github.com/pyreadline3/pyreadline3)             |
| python-dateutil     | 2.9.0.post0  | Apache Software License; BSD License | [Github](https://github.com/dateutil/dateutil)   |
| python-docx         | 1.1.2        | MIT License          | [Github](https://github.com/python-openxml/python-docx)          |
| python-multipart    | 0.0.20       | Apache Software License | [Github](https://github.com/Kludex/python-multipart)          |
| pytz                | 2024.2       | MIT License          | [HP](http://pythonhosted.org/pytz)                               |
| requests            | 2.32.3       | Apache Software License | [HP](https://requests.readthedocs.io)                         |
| rich                | 13.9.2       | MIT License          | [Github](https://github.com/Textualize/rich)                     |
| regex                       | 2024.11.6   | Apache Software License      | [Github](https://github.com/mrabarnett/mrab-regex)                             |
| ruff                | 0.8.4        | MIT License          | [HP](https://docs.astral.sh/ruff)                                |
| safehttpx                   | 0.1.6       | MIT License    | [Github](https://github.com/gradio-app/safehttpx)                              |
| safetensors                 | 0.4.5       | Apache Software License  | [Github](https://github.com/huggingface/safetensors)                           |
| semantic-version    | 2.10.0       | BSD License          | [Github](https://github.com/rbarrois/python-semanticversion)     |
| shellingham         | 1.5.4        | ISC License (ISCL)   | [Github](https://github.com/sarugaku/shellingham)                |
| six                 | 1.16.0       | MIT License          | [Github](https://github.com/benjaminp/six)                       |
| smart-open                  | 7.1.0       | MIT License   | [Github](https://github.com/piskvorky/smart_open)                              |
| sniffio             | 1.3.1        | Apache Software License; MIT License | [Github](https://github.com/python-trio/sniffio) |
| spacy                       | 3.8.3       | MIT License    |[HP](https://spacy.io)                                                     |
| spacy-curated-transformers  | 0.3.0       | MIT        | [Github](https://github.com/explosion/spacy-curated-transformers)              |
| spacy-legacy                | 3.0.12      | MIT License     | [HP](https://spacy.io)                                                     |
| spacy-loggers               | 1.0.5       | MIT   |[Github](https://github.com/explosion/spacy-loggers)                           |
| srsly                       | 2.5.0       | MIT License    | [Github](https://github.com/explosion/srsly)                                   |
| srt                 | 3.5.3        | MIT License          | [Github](https://github.com/cdown/srt)                           |
| starlette           | 0.41.3       | BSD License          | [Github](https://github.com/encode/starlette)                    |
| sympy               | 1.13.1         | BSD License          | [HP](https://sympy.org)                                          |
| thinc                       | 8.3.3       | MIT License       | [Github](https://github.com/explosion/thinc)                                   |
| tokenizers          | 0.20.0       | Apache Software License | [Github](https://github.com/huggingface/tokenizers)           |
| tomlkit             | 0.12.0       | MIT License          | [Github](https://github.com/sdispater/tomlkit)                   |
| tqdm                | 4.66.5       | MIT License; Mozilla Public License 2.0 (MPL 2.0)  | [HP](https://tqdm.github.io)       |
| torch                       | 2.1.2+cpu   | BSD License                                       | [HP](https://pytorch.org/)                                                 |
| torchaudio                  | 2.1.2+cpu   | BSD License                                       | [Github](https://github.com/pytorch/audio)                                     |
| torchvision                 | 0.16.2+cpu  | BSD                                               | [Github](https://github.com/pytorch/vision)                                    |
| transformers                | 4.47.1      | Apache Software License                           | [Github](https://github.com/huggingface/transformers)                          |
| typer               | 0.12.5       | MIT License          | [Github](https://github.com/fastapi/typer)                       |
| typing_extensions   | 4.12.2       | Python Software Foundation License | [Github](https://github.com/python/typing_extensions) |
| tzdata              | 2024.2       | Apache Software License | [Github](https://github.com/python/tzdata)                    |
| urllib3             | 2.3.0        | MIT License          | [Github](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)  |
| uvicorn             | 0.31.0       | BSD License          | [HP](https://www.uvicorn.org/)                                   |
| wasabi                      | 1.1.3       | MIT                                               | [Github](https://github.com/explosion/wasabi)                                  |
| weasel                      | 0.4.1       | MIT License                                       | [Github](https://github.com/explosion/weasel/)                                 |
| websockets          | 12.0         | BSD License          | [Github](https://github.com/python-websockets/websockets)        |
| wheel                | 0.44.0       | MIT License          | [Github](https://github.com/pypa/wheel/blob/main/LICENSE.txt)      |
| wrapt                       | 1.17.0      | BSD License                                       | [Github](https://github.com/GrahamDumpleton/wrapt)                             |
