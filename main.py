import time

from pymongo import MongoClient
import pandas as pd
import re



def categorize_complexity_keywords(code, language):
    if language == "Python":
        # Define keywords for each category
        easy_keywords = ['Set' , 'Tuple' , 'tuple' , 'dictionary' , 'loop' , 'comprehension' , 'indexing' , 'slicing' , 'lambda' , 'filter' , 'zip' , 'reducebits' , 'float', "__future__","abc","argparse","atexit","base64","binascii","bisect","calendar","contextlib","copy","csv","datetime","decimal","enum","fileinput","getpass","gzip","importlib","inspect","logging","openpyxl","operator","pprint","pygments","pytz","random","tempfile","textwrap","time","timeit","traceback","urllib","warnings"]
        medium_keywords = ['Matplotlib' , 'scipy' , 'seaborn' , 'regex' , 'regular' , 'Git' , 'expression' , 'subprocess' , 'JSON' , 'vectorisation' , 'vectorizationwav' , 'mp3' , 'string buffer' , 'MySQL' , 'ASN' , 'TypeError' , 'overload' , 'indentation error' , 'Math range errorInterpreter' , 'pip' , 'range' , 'bytes' , 'NumPy' , 'numpy' , 'Numpy' , 'Pandas' , 'OOPS' , 'Generator' , 'Decorator' , '__enter__' , 'object' , 'file Handling' , 'bash' , 'array' , 'Array' , 'OS' , 'datetime' , 'floating point division' , 'ASCII' , 'tar' , 'docstring' , 'sqlalchemy' , 'sqlite' , 'SQLite',"ast","asyncio","bz2","click","collections","colorama","configparser","cryptography","decorator","difflib","fire","functools","glob","hashlib","http","inflection","io","IPython","json","jsonschema","locale","lxml","math","matplotlib","mock","nbformat","optparse","os","pathlib","pickle","platform","profile","psutil","pydoc","re","requests","sched","scipy","seaborn","select","setuptools","shlex","six","sqlalchemy","sqlite3","ssl","statistics","string","struct","subprocess","sys","termcolor","types","typing","uuid","weakref","webbrowser","xmltodict","auth","av","bs4","builder"]
        hard_keywords = ['Django' , 'Flask' , 'Pyqt' , 'tkinter' , 'pygame' , 'tcp' , 'requests' , 'regression' , 'multithreading' , 'multi-threading' , 'Django session' , 'Django Authentication' , 'Memory Management' , 'Django Middleware' , 'Django Form' , 'Asynchronous' , 'Syncronous' , 'Multiple database' , 'vectorisation' , 'vectorization' , 'cluster' , 'KNN' , 'boto3' , 'aws' , 'garbage collection' , 'mro' , 'GIL' , 'google api' , 'azure' , 'BeautifulSoup' , 'PIL' , 'JavaScript' , 'PHP' , 'Java' , 'telnet' , 'Jinja2' , 'SHA' , 'tree' , 'linkedlist' , 'queue' , 'stack' , 'MacOS' , 'initialisation' , 'cursor' , 'symbolic link' , 'NLTK' , 'eggs' , 'UnboundLocalError' , 'SHA512' , 'href' , 'HTML', "boto","codecs","concurrent","confuse","ctypes","flask","fnmatch","h5py","itertools","jinja2","joblib","markdown","multiprocessing","networkx","nltk","numba","numpy","pandas","paramiko","pdb","plistlib","PyQt5","pytest","queue","shutil","signal","socket","sympy","tensorflow","test","threading","tkinter","toolz","tqdm","tty","twisted","unittest","websocket","adafruit_ble.advertising","adafruit_ble.advertising.standard","adafruit_ble.attributes","adafruit_ble.characteristics","adafruit_ble.characteristics.int","adafruit_ble.services","adafruit_ble.uuid","aeon.forecasting.exp_smoothing","aeon.forecasting.model_selection","aeon.utils._testing.forecasting","aeon.utils.validation._dependencies","aiida.manage.tests.unittest_classes","aiida.plugins","aiida_quantumespresso_magnetic.cli","aiocoap","aiocoap.cli.rd","aiofiles","aiogram","aiogram.types","aiohttp","aiohttp.web_exceptions","aiohttp_security","aiohttp_security.abc","aiohttp_session","aiohttp_session.cookie_storage","airflow","airflow.api_connexion.exceptions","airflow.api_connexion.parameters","airflow.api_connexion.schemas.enum_schemas","airflow.configuration","airflow.exceptions","airflow.hooks.base","airflow.hooks.jdbc_hook","airflow.models.dagrun","airflow.operators.dummy","airflow.utils","airflow.utils.context","airflow.utils.trigger_rule","airflow.utils.types","alembic","allure","ament_index_python.packages","ansible.utils.display","apmec","apmec.agent.linux","apmec.common","apmec.conductor.conductorrpc","AppiumFlutterLibrary.finder","AppiumFlutterLibrary.keywords.keywordgroup","arcade","asdf.tagged","asimov.event","asimov.pipeline","asimov.pipelines.rift","assumptions.log_items","Atom2Vec.EnvMatrix","Atom2Vec.Magpie_elemental_features","Atom2Vec.periodic_table","bert","botbuilder.core","botbuilder.schema","boto.s3","boto.s3.connection","boto3","boto3.session","botocore","bpy","bson"]
        custom_keywords = ["abex","abex.bayesopt","abex.compute_optima","abex.dataset","abex.optimizers.bayes_optimizer","aeskeyschedule","Agent","agents.navigation.agent","agents.navigation.controller","airview_api.blueprint","airview_api.helpers","airview_api.schemas","airview_api.services","algo","alpharotate.libs.models.backbones","alpharotate.libs.models.backbones.efficientnet","alpharotate.libs.models.necks","alpharotate.utils.pretrain_zoo","analyser","anymail.exceptions","api.colors","api.emulation","api.exceptions","api.snippet","apis_core.apis_entities.models","apitools.base.py","app","app.app","App.BridgeGrades.Output.grade_reporter","app.core","app.core.config","app.core.enum.api_name","app.core.goodreads","app.core.pagination","app.event_handler","app.extensions","app.models","app.request_models.prediction_model","app.routes.businesses.controller.alerts","app.routes.businesses.controller.business","app.routes.businesses.controller.business_metrics","app.routes.businesses.controller.business_trends","app.routes.sample_module.controller","app.routes.socialmedia.controllers","app.routes.users.controllers.user","app.schema","app.service","app.service.base_service","app.services.prediction_services","app.views","application.inference.services.model_utils_service","apps.core.models","arenadata_pylint_plugin.assertion_message","arg_utils","args","artemisapi.response","artemislib.aws","Atom2Vec.AE","attack_wrapper.attack_wrapper","attacks.pytorch","attacks.utils","audionews.models","auto_scan_test","autotransform.validator.base","autovideo.base.augmentation_base","autovideo.utils","ava_utils","azext_arcdata.core.constants","azext_arcdata.kubernetes_sdk.models.dict_utils","b2u","banal","banner","base","base_dataset","BaseStiefelMetric","BaseTokenizer","batch_evaluator","behaviours.content_types","berries.models","berries.serializers","bgdev.utils.controler","bhh","bitfactory.cli.create","ble_monitor.ble_parser","bln","bloodnet50","booster","bot","bqat_core.iris","brain_automl.efficientnetv2","brax.training","brax.training.types","btsocket","building"]
        # Combine all keywords
        all_keywords = easy_keywords + medium_keywords + hard_keywords + custom_keywords

        # Define a dictionary to store the category of each keyword
        keyword_categories = {}

        # Iterate through each category and check for the presence of keywords
        for category, keywords in zip(['Hard','Medium','Easy', "Custom"], [hard_keywords,medium_keywords, easy_keywords, custom_keywords]):
            for keyword in keywords:
                # Create a regex pattern for the keyword
                pattern = re.compile(r'\b{}\b'.format(keyword), flags=re.IGNORECASE)

                # Check if the keyword is present in the code
                if re.search(pattern, code):
                    keyword_categories[keyword] = category

        # Determine the overall category based on the most complex keyword found
        if 'Hard' in keyword_categories.values():
            return 'Hard', next((k for k, v in keyword_categories.items() if v == 'Hard'), None)
        elif 'Medium' in keyword_categories.values():
            return 'Medium', next((k for k, v in keyword_categories.items() if v == 'Medium'), None)
        elif 'Easy' in keyword_categories.values():
            return 'Easy', next((k for k, v in keyword_categories.items() if v == 'Easy'), None)
        elif 'Custom' in keyword_categories.values():
            return 'Custom', next((k for k, v in keyword_categories.items() if v == 'Custom'), None)
        else:
            return 'Other', None
    elif language == "Java":
        # Define keywords for each category
        easy_keywords = ["Strings","Searching","Sorting","Linked List","Stacks","Queues","Hashset","Hashmap","Binary Trees","Binary Search Trees","Heap","Arrays","Stream API","Exception handling","Inheritance","OOPS","Math operations","Method overridding","Method Overloading","Encapsulation","Constructors","Linked Lists","Lists","Method overriding","Interface","Abstraction","Polymorphism"]
        medium_keywords = ['Calendar' , 'List', 'Map' , 'JSP' , 'Mockito' , 'MangoDB' , 'JDBC' , 'Connection' , 'Table']
        hard_keywords = ['Spring' , 'spring security' , 'Spring data', 'Spring session', 'ORM' , 'Spring Data' , 'MVC' , 'Controller' , 'bean' , 'LDAP' , 'Apache Kafka' , 'Spring Batch' , 'Annotation' , 'Spring boot' , 'Spring rest' , 'Struts' , 'AOP' , 'Aspects' , 'Context' , 'JMS' , 'Transaction' , 'OXM' , 'POJO' , 'DAO' , 'Repositories' , 'EJB' , 'JBoss' , 'Dependency' , 'injection' , 'webmvc' , 'IOC' , 'singleton' , 'autowired' , 'component' , 'scan' , 'AspectJ' , 'pointcut' , 'JNDI' , 'proxy' , 'Template' , 'Datasource' , 'Persistence' , 'Entity' , 'Dispacher' , 'requestmapping' , 'Hibernate' , 'session' , 'sessionfactory' , 'HQL' , 'criteria' , 'Named query' , 'caching' , 'Dialects' , 'SET' , 'Bag' , 'one to one' , 'one to many' , 'Lazy' , 'HCQL' , 'JPA' , 'Android' , 'JText' , 'JLabel' , 'JavaFx' , 'Servlet' , 'Goolgle analytics' , 'Apache API' , 'Scala' , 'controller', 'JPA' , 'Mapping']

        # Combine all keywords
        all_keywords = easy_keywords + medium_keywords + hard_keywords

        # Define a dictionary to store the category of each keyword
        keyword_categories = {}

        # Iterate through each category and check for the presence of keywords
        for category, keywords in zip(['Hard','Medium','Easy'], [hard_keywords,medium_keywords, easy_keywords]):
            for keyword in keywords:
                # Create a regex pattern for the keyword
                pattern = re.compile(r'\b{}\b'.format(keyword), flags=re.IGNORECASE)

                # Check if the keyword is present in the code
                if re.search(pattern, code):
                    keyword_categories[keyword] = category

        # Determine the overall category based on the most complex keyword found
        if 'Hard' in keyword_categories.values():
            return 'Hard', next((k for k, v in keyword_categories.items() if v == 'Hard'), None)
        elif 'Medium' in keyword_categories.values():
            return 'Medium', next((k for k, v in keyword_categories.items() if v == 'Medium'), None)
        elif 'Easy' in keyword_categories.values():
            return 'Easy', next((k for k, v in keyword_categories.items() if v == 'Easy'), None)
        else:
            return 'Other', None
    elif language == "JavaScript":
        easy_keywords = ['array', 'string', 'objects', 'div', 'element', 'object', 'shuffle',
                         'prevent default behaviour', 'count', 'replace', 'setTimeout()', 'input element', 'checkbox',
                         'version', 'ECMA', 'div', 'window', 'length', 'list', 'array', 'string', 'validate fields',
                         'replace string', 'Loading image', 'Viewport height', 'Maximum and minimum values',
                         'element functions', 'var', 'try', 'catch', 'for', 'if else', 'var', 'array', 'try', 'catch',
                         'methods', 'map', 'reduce', 'filter', 'URL', 'bitwise', 'scrollbar', 'Focus', 'Keys',
                         'Onclick', 'SVG', 'Event handlers', 'initProgressSteps function', 'Kyu 6', 'Task 5',
                         'Office.onReady', 'Lazy load', 'API', 'background', 'function setBtnActive', 'incrementString',
                         'Your order, please', 'accessBody', 'module', 'Adapter pattern', 'Business Logic', 'let',
                         'foo function', 'Iterators', 'encoding', 'Register allocation', 'language texts',
                         'Unlucky Days Calculation Function', 'closures', 'initRegister',
                         'SQLite Database Function (run)', 'game', 'Rover', 'append', 'async function', 'component',
                         'Generate OTP', 'createElf', 'beforeRouteUpdate', 'try', 'updateAsset', 'crearIterador',
                         'rows', 'underscore', 'class ToyVue', 'lista', 'isPrime function', 'diffDays Function',
                         'carrito (cart)', 'head', 'block', 'loadData function', 'export default', 'mysql',
                         'createCanvas', 'Cache savings', 'new Date().getDay()', 'Preloading', 'Internationalization',
                         'function', 'Game', 'supportsFetch', 'Modal', 'arguments', 'request-animation-frame.js',
                         'Proxy Data Function (proxyData)', 'Duration', 'onHear function', 'Arrays', 'User validation',
                         'loop', 'Local Storage and Database Functions', 'Kaboom', 'import', 'Account Balance Function',
                         'animal object', 'colorMode', 'difficulty', 'compose', 'accessStop', 'addToView function',
                         'clouds', 'randomIntegerFromInterval', 'Hamburger JS', 'middleware',
                         'function left_is_smaller', 'fallback', 'Staircase', 'getTimeDifference', 'cardContainer',
                         'Rabbit game', 'Base', 'function timer', 'array',
                         'Stack Trace Description Function (stackTraceDescription)', 'rellotge', 'Redux action',
                         'input', 'static', 'initGame', 'constructor', 'function createLinkedList',
                         'singletonPattern function', 'checkFocus', 'Ninja function', 'rabbitMovement', 'GraphQL',
                         'gql', 'Factory function', 'ApolloClient', 'getElementById', 'min function', 'REST config',
                         'Redux', 'function left_is_greater', 'Prime numbers', 'order', 'website title',
                         'toggle button', 'cols', 'Private variables', 'replace', 'Algorithm', 'tMax',
                         'Text Validation Function (validText)', 'bindActionCreators',
                         'Phaser Game Object Class (Enemy2)', 'Timer', 'Beep Boop Business Logic Function (beepBoop)',
                         'Fibonacci sum', 'configuration', 'setFavicon', 'function initLocalStorage',
                         'document.createElement', 'radius', 'string manipulation', 'node-fetch', 'setup',
                         'AdvancedShipping', 'duration', 'workbook', 'toCamelCase', 'UserCertificateService', 'logic',
                         'environment', 'path', 'cloudflare_recaptchaPass', 'filter', 'Sum', 'doubles',
                         'portsWithNewIdsData function', 'addCoreAsset function', 'sumFibonacci function', 'Stack',
                         'i18n', 'initialization', 'Ports', 'Particle class', 'parameters', 'party activities', 'frame',
                         'func', 'findSum', 'getTimeRemaining', 'postLogoutUser function',
                         'Age Calculation Function (getMyAgeDate)', 'recursion', 'DOM', 'spaces', 'new IDs',
                         'Player health', 'stairCase', 'Array', 'function mouseClicked', 'Fruit Market', 'insertTail',
                         'Import', 'function setup', 'separatePositive', 'createMicrofone', 'rabbit movement',
                         'Cart Management Functions (add, remove)', 'babelHelpers', 'function isWeekend', 'Task 9',
                         'function draw', 'Window', 'Discord selfbot', 'exports', 'fontSize',
                         'Lv. 1 Algorithm Solution (solution)', 'selectors', 'solution', 'Clone machine',
                         'function _left_is_greater', 'functions', 'logout request', 'recordFile', 'AppController',
                         'Square Digits Function (squareDigits)', 'setTitle', 'interval', 'cloneMachine function',
                         'document.addEventListener', 'document.querySelector', 'Progress steps', 'findNb',
                         'Playwright module', 'class UserInfo', 'problem solving', 's', 'refs', 'class Tetrominos',
                         'changeColor', 'ShippingAdapter', 'hoverFontChange', 'accessStart', 'interopRequireDefault',
                         'constants', 'options saving', 'fromJson', 'Bubble Sort Function', 'readlineSync',
                         'Random ID Generation Function', 'class Todo', 'Date', 'function test_result',
                         'Module imports', 'Chrome storage', 'colors', '# characters', 'conditionals', 'N',
                         'Local storage', 'timerId', 'chapters', 'speed', 'Database', 'Shipping', 'classList',
                         'fetchImg', 'HTML', 'lacuna_lazy_load', 'jwt', 'time in milliseconds',
                         'errorHandlerMiddleware', 'posix-style', 'Math', 'UI elements', 'error handling', 'Delay',
                         'PartyActivities', 'define', 'navigate', 'sortByHeight', 'querySelectorAll', 'textContent',
                         'Form validation', 'File system', 'New', 'Guessing game', 'images', 'HTTP request',
                         'function isLoggedIn', 'Laplace transform', 'measurement', 'remove', 'controllers',
                         'game contexts', 'Singleton pattern', 'onclick', 'save to JSON file', 'fs-extra',
                         'localStorage.getItem', 'countdown', 'callback function', 'Slider', 'DropList/Input',
                         'fetchText', 'co-ordinates', 'localStorage.setItem', 'actions', 'Export to Excel',
                         'save_options function', 'Task 7', 'function testFunction', 'camel case', 'problems',
                         'Discord.js-selfbot-v11', 'Queue', 'Event handling', 'easy', '$', 'Build a pile of Cubes',
                         'data loading', 'duplicateEncode', 'SVG', 'line', 'calcularMediaAritmetica', 'intro',
                         'toMeasureHealth function', 'words', 'special problems', 'Minimum', 'email', 'React',
                         'require', 'DOMContentLoaded', 'checkIfRabbitFound', 'favicon', 'querySelector',
                         'Math Power Functions (makePower, makeSalary)', 'dash', 'toggleFunc', 'Traveling',
                         'Shopping Cart Management Functions', 'A', 'custom spin component', 'call', 'isSubsequence',
                         'document.cookie']
        medium_keywords = ['REgExp', 'prototype', 'contenteditable', 'RegExp', 'SVG elements', 'Callback function',
                           'PHP', 'JSTL Variable', 'Plugins', 'RegExp', 'automatically', 'Date parsing',
                           'Internet Explorer', 'AJAX', 'RegExp', 'RegExp', 'instanceof', 'Regular Expression',
                           'getSolidDataset', 'Express Router Setup with StatusRouter Class', 'jslint', 'Express',
                           'Iphone', 'link', 'inorder', 'getAllUser',
                           'Leetcode Container With Most Water Problem Solution', 'Admin Middleware Function', 'ripRaw',
                           'ipcRenderer', 'viewing link', 'parseEther', 'getXhr Function', 'usersRoute', 'Contador',
                           'WebSocket onMessage Function', 'getThis', 'initDistPath', 'src',
                           'React Components (DeliveryInfo', 'authorizeUser', 'Config', 'CSS', 'class', 'Canvas Class',
                           'bootstrap', 'readCSV', 'process', 'get', 'square', 'decorator pattern', 'ipcMain',
                           'Group Trial Ended Function (group_trial_ended)', 'Thought', 'AnteiGuild',
                           'DeliveryCondition', 'babel', 'windowCloseBefore',
                           'Date Function to Get the Name of the Day 4 Days Ago', 'downPayment Function', 'initSrcPath',
                           'autoprefixer', 'zip Function', 'watch', 'muteButton', 'getUsers', 'Bus', 'generateToken',
                           'BinarySearchTree', 'Layer', 'getModulesPaths Function', 'tree data', 'Popups',
                           'console.log', 'error handling', 'id', 'authServices', 'curry', 'frontend', 'fs', 'file',
                           'Client', 'sizeMaze', 'update', 'V.1', 'merge2', 'import', 'del',
                           'Event Class for Event Management', 'apiRequest', 'jQuery', 'h-index', 'HasOwnProperty',
                           'compose1', 'OpenAIApi', 'ethers', 'Loader Class for Memes Loading', 'htmlmin', 'React',
                           'getPeriodTimes Function', 'printing', 'var', 'attachPopstateEventListenerToLink',
                           'mongoose', 'login', 'connectedCallback', 'parallel', 'Order', 'Preview',
                           'document.getElementById', 'getUserDataSources', 'withSentryConfig', 'index.scss',
                           'cycleInGraph Function', 'FOAF', 'traverse', 'TempTracker', 'nextConfig', 'Consent class',
                           'Node.js', 'addToZero Function', 'validateUser', 'Node', 'getStringNoLocale', 'Error',
                           'ripFast', 'validateCategoryId', 'move', 'MatrixGame', 'uglify', 'compareKeys',
                           'LastUpdate Web Component (Custom Element)', 'websocket', 'fillMatrix',
                           'defLambda Function with AST Manipulation', 'async function', 'validateLogincredentials',
                           'purgecss', 'nativeTheme', 'joi', 'Partial Function Implementation (ES6 and ES5)',
                           'getDefaultSession', 'ProcessGUI', 'propTypes', 'cssmin', 'Configuration',
                           'componentDidMount', 'authentication', "use strict'", 'saveUpdate', 'checkAuth',
                           'isPowerOfTwo', 'Import', 'showErrors', 'Atom', 'keccak256', 'Toggle', 'MuteButton',
                           'Curry Function', 'add', 'themeCallback', 'formatFileSize', 'require', 'E', 'concat', 'Gulp',
                           'Authorize', 'AimeosAccountProfile Object with Event Handlers', 'module.exports',
                           'handleIncomingRedirect', 'Array', 'StatusCodes', 'User', 'document.querySelector', 'Scene',
                           'function', 'button', 'insert', 'renderProds', 'Ground',
                           'knightItem and MGTItem Classes Extending Item Class', 'AbuseMonitor Class', 'maze',
                           'display', 'BoteDeGuerra', 'pool', 'Duplicate tozanJoho Function', 'ESAbstract', 'minify',
                           'ripView', 'ripNelo', 'Grub', 'BrowserWindow', 'initCallback', 'Ipad', 'all', 'ReactDOM',
                           'Menu', 'observedAttributes', 'buildsMessage Function', 'Logging', 'outPath', 'const',
                           'getAllOrders', 'same number of digits', 'logAction', 'Reference Class for AST Manipulation',
                           'Console input/output', 'ripToons', 'App', 'WatchClass', 'Structures',
                           'isLowerCased Function', 'ripExtra', 'TabPanel)', 'setSize', 'attributeChangedCallback',
                           'Display Class for Spider Game', 'insertBookmark', 'sorting', 'getShopClass', 'fn',
                           'MapFactory Class', 'random', 'IpcRendererUtils', 'UserController', 'Preact',
                           'Object with methods', 'Mouse Interaction on Keyboard Element',
                           'Middleware Function for MQTT Communication', 'constructor', 'ContactoController',
                           'electron', 'DropdownHeader Component', 'N', 'useref', 'generateTopicCover', 'Solid',
                           'addEventListener', 'autoPrefixerHTML', 'JavaScript Code for Timer Control', 'Router',
                           'initConfigPaht', 'File system', 'lodash', 'Express Router Setup with setupRoutes Function',
                           'CSV', 'AppError', 'Solution Function for Leetcode Problem', 'lass', 'extends', 'getThing',
                           'currentRow', 'getCommonCharacterCount', 'async', 'Transaction', 'dest',
                           'isUpperCased Function', 'box', 'isWayLeft', 'Component',
                           'updateBuildTargets Function Using devkit and nrwl', 'static', 'Bee', 'DateModel',
                           'MoreArtworks', 'getPokemons', 'task', 'axios', 'extend',
                           'Leetcode Move Zeroes Problem Solution', 'h', 'series', 'MD5', 'Star',
                           'Change Function for Pixel Manipulation', 'LeetCode', 'responsiv', 'Row',
                           'Owl Carousel setup', 'p5.js Setup Function', 'main', '_events', 'getAllUsers', 'jsx',
                           'Site Preloader preloader Function', 'Sharing modal', 'timestampToDate', 'StartScreenBall',
                           'fetch', 'rename', 'CustomShaderMaterial Class', 'BinaryReader', 'checkGameExists', '$on',
                           'Smallest number', 'ES6 class', 'Plugins', 'VCARD', 'draw', 'product list', 'console.log',
                           'scale', 'WidthType', 'useRender', 'constructor', 'Posts', 'reset', 'CONFIG', 'computerMove',
                           'Main', 'typewriter Function for Animated Text', 'GenericExtrinsicV4', 'reactive', 'let',
                           'create', 'dAppClient', 'User Class (with findAll and create methods)', '#ariaLabelDefault',
                           'loadSpriteSheet', 'optionGroupProps', 'getSecretKey Function', 'QS_MODE_WHITELIST',
                           'getUsersSavedItems Function', 'classDecorator', 'sendData', 'Overlay',
                           'require keyword of Node.js', 'exec', 'Three.js', 'getResponse', 'BlockchainAttr', 'setup',
                           'useNamespace', '_mountedHook', 'setColumn', 'App', 'get dronesData', 'PAGE_WIDTH', '_',
                           'UserModule', '$', 'CHESS', 'export function loadKoopa', 'this', 'Edit', 'submiting',
                           'getCookieNames', 'ConnectWallet', 'getRootFontSize', 'Box', 'has', 'setLabel', 'toJSON',
                           'render', '_preventQueryParametersConflict', 'useCallback', 'draw', 'State', '_getCronJobs',
                           'Form', 'updateMetadataSidecar', 'Handling Form Submission with handleSubmit Function',
                           "'dotenv/config'", 'loadAudioBoard', 'CustomCacheKey', 'animate', 'lolplaysEdit',
                           'intervalIndex', 'db', 'random', 'Interpreter', 'User', 'ResponseErrorWrapper', 'CANVAS',
                           'import', 'createTeam', 'edit', 'ALGEBRAIC_NOTATION', 'Page', 'lolplaysCreate', 'Struct',
                           'init Function (loading users from the database)', '_2PI', 'onSubmit', 'Sidecar',
                           'export const', 'AJAX', 'SidecarBody', 'fullWeeksNumberInMonth', 'wrapExports', 'initialize',
                           'startCronJobs', 'init', 'router', 'ruler', 'emitter', 'playback',
                           'ForbiddenAlphaMaterialSheet', 'UserName', 'effects', 'drawKoopa', 'registerResponse',
                           'convertToTensor', 'updateTenant', 'return', 'message',
                           'updateUserPermissionsNull Function for Database Update', 'Search', 'Pop', 'transaction',
                           'QUERY_PRODUCT_BY_NAME', 'RegExp', 'addTenant', 'Btns', 'QS_MODE_BLACKLIST',
                           'connectedCallback', 'get', 'toggle', 'lolplaysNew', 'commentLike', 'PERMISSION_KEY',
                           'setStyle', 'document.getElementById', 'var', 'BreadthFirstSearchObjArr', 'getListData',
                           'dom', 'Navigation', 'interpret', 'async function', 'threads', 'get url',
                           'getFridaysOfMonth', 'fadeOutMusic', 'Util',
                           'getLatestMatch Function for Fetching Football Match Data', 'Context', 'tryEnsureIndex',
                           'NewestGatherings', 'MongoDB', 'export default', 'defaultOptions', 'closeDevice',
                           'get Function for Retrieving a Key from Object:', 'SetAutoCommitModePacket Function',
                           'MainModel', 'FILTER_DEFINITION', 'NodeMaterialBlockConnectionPointTypes', 'require',
                           'getCurrentInstance', '#content', 'isU8a', 'update', "'./App.css'", 'flatten',
                           'beatsPerMeasure', 'NOptionGroup', 'GenericExtrinsicV4',
                           'MaterialTable Class with CRUD Operations', 'create_Categories Function', 'jwt', 'Base',
                           'getTeams', 'toRaw', 'handleGenerateListFromResponse Function', 'GatheringPlaceGraphics',
                           'removeFav', '__extends', 'Sequelize', 'axios', 'getInstanceWithAuth', 'beautilize',
                           'IgApiClient', 'Queue Class', 'ExifReader', 'getAuction', "'./time.js'", 'width',
                           'MENU_STORAGE', 'useEffect', 'createPagination', 'interpretBinary', 'tip',
                           'retrieveLyrics Function', 'Message', 'THEME_MODE_KEY', 'BaseModule', 'unlike', 'create',
                           'appState', 'getinfo', 'NodeMaterialBlock', 'exec Function for Child Process', 'inject',
                           'deleteTeam', 'ticksPerBeat', 'determineStartingCoordinates', 'showDeviceName',
                           'BestReviews', 'addBid', 'getUserByName Function', 'localStorage.setItem',
                           'excludeAllQueryParameters', 'Emitter', 'data', 'lit-html', 'DataUtils', 'RegisterClass',
                           'gbk2buffer', 'Popconfirm', 'Game', 'eventBridge', 'quickInitDevice', 'nls.js', 'TOKEN_KEY',
                           'ForbiddenAlphaItemSheet', 'makeShooter', 'using MongoDB with Mongoose (Node.js',
                           'scraper Function Using puppeteer and cheerio', 'Show Class with middleware Method',
                           'Auction', 'SunComponent', 'scaleVal', 'clamp', 'hideLoading', 'QUERY_PRODUCTS',
                           'AbstractStorage', 'setGlobalSampleVolume', 'searchProduct',
                           'Webpack Configuration with configureWebpack', 'declareLambda', 'computeWeightedLoss',
                           'Body Parser', '#isToggle', 'won', 'to', 'toRefs', 'declareVar', 'Entity', 'TEMPLATE_MODEL',
                           'interpretCall', 'validate', 'defineComponent', 'ref', 'onShow', 'createKoopaEntity',
                           'addFav', 'useEffect', 'routeFrame', 'fs', 'inquirer', 'test Function', 'style',
                           'tick Function for Clock App', 'new', 'PCT_REG', 'instanceNoAuth', 'createAndSignin',
                           '_position', 'RefractBlock', 'html', 'Scheduler Function', 'PAGE_WIDTH_HORIZONTAL',
                           'Express)', 'MAX_MESSAGES_SHOW', 'watch', 'expectDemoUserBasicFields', 'instance',
                           'CreateModal', 'crons', 'MENU_KEY', 'useQuery', 'Chess', 'isMonthLong', 'Config',
                           'preCronJobHook', 'start Function for Employee Tracker', 'buildSidecarMetadata', 'useState',
                           'getPackageName Function Using path', 'AdjacencyGraphObj', 'editor', 'exampleInput',
                           'provide', 'settingTime', 'CronJobs', 'compiler', 'like', 'DB_NAME', 'Index',
                           'module.exports', 'convert Function Using meriyah and estraverse', 'updateDrone',
                           'getDB Function (MongoDB Connection)', 'Route Initialization Function (initRoutes)',
                           'getRatingsByJobId Function', 'ig', 'expect', 'Player Factory Function', 'SunController',
                           'randomQuote Function', 'Input', '#ariaLabelActive', 'THEME_KEY', 'Express',
                           'AuthValidation Class with createAuth Method', 'queryTenant', 'Particle', 'BadRequestError',
                           'dAppClient and ConnectWallet Functions', 'TOKEN_STORAGE', 'dayjs', 'set', 'demoUser',
                           'NodeMaterialBlockTargets', 'list', 'EXTRINSIC_VERSION', 'Reduction', 'connect', 'products',
                           '#shadow', 'THREE', 'function', 'puzzleInput', 'commentUnlike',
                           'SliderService Class with update Method', 'tipCount', 'lolplaysShow',
                           'initSchedule Function', "'../math/MathUtils.js'", 'useState', 'webpackPlugins',
                           'queryTenant', 'parse', 'getSubjectList', 'ATVModel', 'CachingStorage', 'lookup',
                           'EventListener', 'replInstance', 'moveValid', 'onMessageReceived', "'vue'", 'AVATAR_SIZE',
                           'useScrollLockManager', 'static toHalfFloat(val)', 'ContentCopyIcon', 'Parse',
                           'lexer Function for Tokenization', 'getDirName Function for Generating Path Names', 'play',
                           'op', 'Toggle Theme Switching with onToggleChange Function', 'Divider', 'input', 'riot',
                           'connentDevice', 'ErrorRegistration', 'log', 'InstancedTile', 'shortestWeekDaysNumber',
                           'NearClosureGatherings', 'EventEmitter', 'getInstance', 'excludeAllQueryParametersExcept',
                           'getArticleDetail', 'storeDB Function', '* as Comlink', 'generateSpreadParticles',
                           'evaluate', 'postCronJobHook', 'createNanoEvents', 'const', 'squaredDifference',
                           'formatDate', 'queryTenantDetail', 'decodeExtrinsic', 'inviteTeam', 'state',
                           'PromoCodeModel', 'fadeInMusic', 'THEME_STORAGE', '_draw', 'sunClass', 'getArticleDetail',
                           'generateWallets Function', 'lolplays Functions (lolplaysIndex', 'swalClasses',
                           'PAGE_ORIENTATION', "from 'docx'", 'StorageType', 'Parser',
                           'Files Class for Source File Generation', 'assertShapesMatch', 'valuesService',
                           'main Function', 'addHours', 'load', 'onMounted', 'position', 'useReducer', 'isActive',
                           'excludeQueryParameters', 'getSubjectList', 'useRef', 'playing', 'addCookie', 'Particle',
                           "'react'", 'NewestReviews', 'wrapError', 'guardMetadataSidecar', 'addHeader', 'LAYOUT_KEY',
                           'editTeam', 'findLastFileByUser', 'namespace', 'IS_GET_MENU_KEY', 'Grid',
                           'meanSquaredError_', 'extends', "'./ScrollLock.scss.js'", 'BaseScorePanel', 'Transform',
                           'createUser Function Using userModel', 'class', 'Redux', 'List', 'clipboard', 'cookie',
                           'DEFAULT_ENCRYPTION_ALGORITHM', 'bpm', 'sayHi', 'Cesium', 'acceptInvite',
                           'Faktur Class (with rvft and pvc methods)', 'ScrollLock', 'setHTML', 'checkStatus Function',
                           'lolplaysUpdate)', 'getAdd', 'Navbar', 'superagent', 'React', 'breakWord',
                           'Functions related to a web application', '* as', 'login', 'findById', 'flattedChildren',
                           'subtractHours']
        hard_keywords = ['google APi', 'Http', 'Rails', 'Android WebView', 'display busy indicator',
                         'regular expression', 'cross-domain', 'Activex', 'Rails', 'document object model',
                         'document object model', 'RegExp', 'HTTP', 'Hash', 'API integration', 'encryption',
                         'cross browser', 'BigNumber', 'Math.round', 'coffescript', 'Cross domain', 'DOM', 'async',
                         'await', 'prototype', 'promises', 'cross-domain', 'Rails', 'jQuery Framework', 'jQuery',
                         'jQuery', 'jQuery', 'JQuery framework', 'brick', 'sqlite3', 'gallery-item.js', 'lodash',
                         'React', 'Vector', 'Express', 'Axios, API interaction', 'Compiler', 'Vue',
                         'React, Axios, Redux', 'NodeJS, Express', 'toBn', 'poker.js', 'bcryptjs', 'HTTP', 'async',
                         'Email', 'gulp', 'React, React Router', 'use strict', 'eslint', 'write', 'React, React-Select',
                         'React, React-Bootstrap, React Router, Axios, Redux', 'DOM', 'Discord', 'Crypto',
                         'Google Maps', 'React, PropTypes, Material-UI, Axios, CSS Styles', 'aws',
                         'React, PropTypes, Button Component', 'Standard', 'Graph']
        # Combine all keywords
        all_keywords = easy_keywords + medium_keywords + hard_keywords

        # Define a dictionary to store the category of each keyword
        keyword_categories = {}

        # Iterate through each category and check for the presence of keywords
        for category, keywords in zip(['Hard','Medium','Easy'], [hard_keywords,medium_keywords, easy_keywords]):
            for keyword in keywords:
                # Create a regex pattern for the keyword
                pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), flags=re.IGNORECASE)

                # Check if the keyword is present in the code
                if re.search(pattern, code):
                    keyword_categories[keyword] = category

        # Determine the overall category based on the most complex keyword found
        if 'Hard' in keyword_categories.values():
            return 'Hard', next((k for k, v in keyword_categories.items() if v == 'Hard'), None)
        elif 'Medium' in keyword_categories.values():
            return 'Medium', next((k for k, v in keyword_categories.items() if v == 'Medium'), None)
        elif 'Easy' in keyword_categories.values():
            return 'Easy', next((k for k, v in keyword_categories.items() if v == 'Easy'), None)
        else:
            return 'Other', None


def extract_imports_python(python_code):
    # Extract import names using regex
    import_names = []

    # Extract import statements using regex
    import_matches = re.finditer(r'\bimport\s+([^\s;]+)\s*;?', python_code)
    from_import_matches = re.finditer(r'\bfrom\s+([^\s]+)\s+import\s+([^\s;]+)\s*;?', python_code)
    from_star_import_matches = re.finditer(r'\bfrom\s+([^\s]+)\s+import\s+\*\s*;?', python_code)

    # Process the import names
    for match in import_matches:
        import_names.append(match.group(1))

    # Process "from ... import ..." statements
    for match in from_import_matches:
        module_name = match.group(1)
        function_names = [name.strip() for name in match.group(2).split(',')]
        import_names.append(module_name)
        import_names.extend([f"{module_name}.{name}" for name in function_names])

    # Process "from ... import *" statements
    for match in from_star_import_matches:
        module_name = match.group(1)
        import_names.append(module_name)

    # Use set to remove duplicates
    keywords = list(set(import_names))

    return keywords


# Function to extract imports from Java code

def extract_imports_java(java_code):
    # Extract import names using regex
    import_names = []

    # Extract import statements using regex
    import_matches = re.finditer(r'\bimport\s+([^\s;]+)\s*;?', java_code)

    # Process the import names
    for match in import_matches:
        import_names.append(match.group(1))

    # Use set to remove duplicates
    keywords = list(set(import_names))

    return keywords

def extract_imports_js(js_code):
    # Extract import names using regex
    import_names = []

    # Extract import names using regex
    curly_brace_matches = re.finditer(r'\bimport\s*{([^}]*)}\s*from\s*[\'"](\S+)[\'"]\s*;?', js_code)
    direct_imports = re.finditer(r'\bimport\s*([^\s;]+)\s*;?', js_code)
    from_imports = re.findall(r'\bfrom\s*[\'"](\S+)[\'"]\s*import\b', js_code)

    # Process the import names from the curly braces
    for match in curly_brace_matches:
        names = [name.strip() for name in match.group(1).split(',') if match.group(1)]
        import_names.extend(names)

    # Process the direct import names
    for match in direct_imports:
        import_names.append(match.group(1))

    # Combine import names from both forms
    import_names += [name for imp in from_imports for name in imp.split('.')]

    # Use set to remove duplicates
    keywords = list(set(import_names))

    return keywords

# Replace the connection string with your MongoDB connection string
connection_string = "mongodb+srv://adityamalik2023:Deloitte@cluster0.j1d4on4.mongodb.net/rlhfDBSubham"

# Connect to MongoDB
client = MongoClient(connection_string)

# Access a specific database
db = client["RM-Annotation-Logs"]

# Access a specific collection in the database
collection = db["annotations"]

# Now you can perform operations on the 'collection' object, such as querying or inserting data


# Example: Query all documents in the collection
query_result = collection.find()

while(True):
    common_list = []
    for results in query_result:
        #print(results)
        data = results
        excel_data = {}
        keywords = []
        category = []
        complexity = []
        # Check if the taskType is 'S1 Review' or 'S2 Review' and language is 'Python'
        if data.get('language') == 'Python':
            keywords = [extract_imports_python(data.get("prompt"))]
            complexity, category = categorize_complexity_keywords(data.get("prompt"), data.get("language"))
            category = [category]
            #print(complexity)

        elif data.get('language') == 'Java':
            keywords = [extract_imports_java(data.get("prompt"))]
            complexity, category = categorize_complexity_keywords(data.get("prompt"), data.get("language"))
            category = [category]
            #print(complexity)
            #print(keywords)
        elif data.get('language') == 'JavaScript':
            keywords = extract_imports_js(data.get("prompt"))
            complexity, category = categorize_complexity_keywords(data.get("prompt"), data.get("language"))
            category = [category]
            #print(complexity)
        else:
            pass
        if "complexity" not in data and "keywords" not in data:
            collection.update_one(
                {"_id": data["_id"]},
                {
                    "$set": {
                        "complexity": complexity,
                        "keywords": category
                    }
                }
            )
        data["keywords"] = keywords
        data["complexity"] = complexity
        excel_data = {
            "annotation ID": data.get('annotationId'),
            "annotatorEmail": data.get('annotatorEmail'),
            "Language": data.get("language"),
            "complexity": complexity,
            "category": category,
            "keyword": keywords
        }
        common_list.append(excel_data)




    # Close the MongoDB connection when done

    time.sleep(900)
client.close()