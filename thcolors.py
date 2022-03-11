import matplotlib.colors as mcolors
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200
def testfunce():
    return
c = {'hina1':"#34BB7E",   # 键山雏
    'hina2': "#c41919",
    'hina3': "#256352",
    'hina4': "#4d1411",
    'keiki1': "#00adf9",    # 袿姬
    'keiki2': "#1a6069",
    'keiki3': "#e3ac36",
    'keiki4': "#e52418",     
    'keiki5': "#89f35b",
    'satori1': "#AB529E",   # 觉
    'satori2': "#6e9fb8",
    'satori3': "#D21A1A",
    'satori4': "#C8903E",
    'koishi1': "#e09c4a",   #恋恋
    'koishi2': "#49c46e",
    'koishi3': "#834c38",
    'koishi4': "#751d6d",
    'kokoro1': "#006E8F",   # 秦心
    'kokoro2': "#B75371",
    'kokoro3': "#FF8F75",
    'kokoro4': "#1C7BE8",
    'satono1': "#cc1092",    # 里乃
    'mai1': "#115939",   # 舞
    'okina1': "#e58a2a",    # 隐岐奈
    'okina2': "#00b25b",
    'okina3': "#c4aa79",
    'okina4': "#644a6e",
    'okina5': "#bace43",
    'okina6': "#ff60c3",
    'okina7': "#00fffe",
    'okina8': "#ff7828",
    'meirin1': "#ae444a",   # 美铃
    'meirin2': "#667728",
    'kanako1': "#e4332d",   # 神奈子
    'kanako2': "#5d3cc3",
    'kanako3': "#d1a267",
    'kanako4': "#44192a",
    'suwako1': "#7d52c8",     # 诹访子
    'suwako2': "#AF7B34",
    'suwako3': "#bd0415",
    'suwako4': "#007e21",
    'junko1': "#0e0a07",    # 纯狐
    'junko2': "#ffa933",
    'junko3': "#ca5fa0",
    'junko4': "#f10017",
    'piece1': "#008ac2",    # 皮丝
    'piece2': "#ff0018",
    'piece3': "#e4ad32",
    'piece4': "#be0075", 
    'piece5': "#964cd8",
    'yuyuko1': "#FA057A",   # 幽幽子
    'yuyuko2': "#6889CC",
    'yuyuko3': "#f60100",
    'yuyuko4': "#10016a",
    'chen1': "#339886",   # 橙
    'chen2': "#7d4439",
    'chen3': "#e13b2d",
    'chen4': "#ea9947",
    'chen5': "#423437",
    'parsee1': "#128134",   # 帕露西
    'parsee2': "#BE8F1A",
    'parsee3': "#4d0e84",
    'parsee4': "#a24809",
    'parsee5': "#2a3bd1",
    'kasen1': "#f25566",    # 华扇
    'kasen2': "#8a991d",
    'kasen3': "#6e2528",
    'suika1': "#dcc098",    # 萃香
    'suika2': "#53248d",
    'suika3': "#e38253",
    'suika4': "#fa413c",
    'shiki1': "#389f72",    # 四季
    'shiki2': "#7070c6",
    'shiki3': "#d7a546",
    'shiki4': "#ce394f",
    'shiki5': "#816653",
    'shiki6': "#2a201f",
    'byakuren1': "#5a2d68",   # 白莲
    'byakuren2': "#DC8A4F",
    'byakuren3': "#010302",
    'byakuren4': "#064000",
    'seija1': "#18161d",    # 正邪
    'seija2': "#ff1b1a",
    'seija3': "#1a0c6b",
    'seija4': "#5f5f5f",
    'yachie1': "#FFE383",   # 八千慧
    'yachie2': "#4F7878",
    'yachie3': "#00520D",
    'yachie4': "#CF3C0D",
    'saki1': "#702700",   # 早鬼
    'saki2': "#000000",
    'saki3': "#5ba797",
    'saki4': "#6d7c99",
    'saki5': "#d66a7e",
     'chimata1': "#22028a",   # 千亦
     'chimata2': "#fa0202",
     'chimata3': "#d17901",
     'chimata4': "#00d65a",
     'chimata5': "#0094e0",
     'chimata6': "#5702b7",
     'chimata7': "#ff00ad",
     'chimata8': "#bab338",
     'megumu1': "#255a86",    # 饭纲丸龙
     'megumu2': "#c7ba1a",
     'megumu3': "#3f077c",
     'misumaru1': "#a49e67",    #玉造魅须丸
     'misumaru2': "#ac0b91",
     'misumaru3': "#ff0000",
     'misumaru4': "#2b0552",
     'misumaru5': "#ffba00",
     'misumaru6': "#00a28e",
     'renko1': "#2d2d2d",   # 莲子
     'renko2': "#f92e41",
     'merry1': "#CF7F1D",   # 梅莉
     'merry2': "#77509e",
     'momoyo1': "#5B7691",  # 百百世
     'momoyo2': "#080808",
     'momoyo3': "#007D41",
     'momoyo4': "#B54000",
     'momoyo5': "#97A019",
     'kogasa1': "#C80F15",  # 小伞
     'kogasa2': "#3B66BA",
     'kogasa3': "#571D55",
     'patchy1': "#592458",  # 帕琪
     'patchy2': "#2D6693",
     'patchy3': "#DE4BD7",
     'patchy4': "#D9AA16",
     'patchy5': "#6956A8",
     'alice1': "#DC812E",   # 爱丽丝
     'alice2': "#D03420",
     'alice3': "#3E6094",
     'reisen1': "#21127D",  # 铃仙
     'reisen2': "#9E0105",
     'reisen3': "#CE7931",
     'reisen4': "#080808",
     'akyuu1': "#952F73",   # 阿求
     'akyuu2': "#52A800",
     'akyuu3': "#850812",
     'akyuu4': "#FAA74D",
     'rinnosuke1': "#a0a0a0",   # 霖之助
     'rinnosuke2': "#2A4D7D",
     'rinnosuke3': "#B53203",
     'rinnosuke4': "#080808"
     
    }
mcolors.get_named_colors_mapping().update(c)

def print_name():
    name_last = 'hina'
    for name_,dict_ in c.items():
        name = name_[:-1]
        if name == name_last:
            continue
        print(name)
        name_last = name
    return
