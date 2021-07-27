from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.',static_url_path='')

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', \
		title = 'キーチェッカー', \
		message = 'コードを選んでください。')
@app.route('/', methods=['POST'])
def post():
    code1 = str(request.form.get('sel1'))
    accidental1 = str(request.form.get('sel2'))
    input1 = code1 + accidental1

    code2 = str(request.form.get('sel3'))
    accidental2 = str(request.form.get('sel4'))
    input2 = code2 + accidental2

    code3 = str(request.form.get('sel5'))
    accidental3 = str(request.form.get('sel6'))
    input3 = code3 + accidental3

    code4 = str(request.form.get('sel7'))
    accidental4 = str(request.form.get('sel8'))
    input4 = code4 + accidental4   

    code5 = str(request.form.get('sel9'))
    accidental5 = str(request.form.get('sel10'))
    input5 = code5 + accidental5

    code6 = str(request.form.get('sel11'))
    accidental6 = str(request.form.get('sel12'))
    input6 = code6 + accidental6
 
    target_original = set()

    target_original.add(input1)
    target_original.add(input2)
    target_original.add(input3)
    target_original.add(input4)
    target_original.add(input5)
    target_original.add(input6)
    #♭を＃に変換
    target = {s.replace('D♭', 'C#').replace('E♭', 'D#').replace('G♭', 'F#').replace('A♭', 'G#').replace('B♭', 'A#') for s in target_original}


    #各キーのよく使われるコード（＃のかわりにsを用いる）
    #メジャーキーのダイアトニックコード（Ⅶm♭-5は除く）
    C_Major = {'C', 'Dm', 'Em', 'F', 'G', 'Am'}
    Cs_Major = {'C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m'}
    D_Major = {'D', 'Em', 'F#m', 'G', 'A', 'Bm'}
    Ds_Major = {'D#', 'Fm', 'Gm', 'G#', 'A#', 'Cm'}
    E_Major = {'E', 'F#m', 'G#m', 'A', 'B', 'C#m'}
    F_Major = {'F', 'Gm', 'Am', 'A#', 'C', 'Dm'}
    Fs_Major = {'F#', 'G#m', 'A#m', 'B', 'C#', 'D#m'}
    G_Major = {'G', 'Am', 'Bm', 'C', 'D', 'Em'}
    Gs_Major = {'G#', 'A#m', 'Cm', 'C#', 'D#', 'Fm'}
    A_Major = {'A', 'Bm', 'C#m', 'D', 'E', 'F#m'}
    As_Major = {'A#', 'Cm', 'Dm', 'D#', 'F', 'Gm'}
    B_Major = {'B', 'C#m', 'D#m', 'E', 'F#', 'G#m'}

    #マイナーキーのダイアトニックコード（Ⅱm-5を除き、Ⅴを加える）
    A_minor = {'Am', 'C', 'Dm', 'Em', 'E', 'F', 'G'}
    As_minor = {'A#m', 'C#', 'D#m', 'Fm', 'F', 'F#', 'G#'}
    B_minor = {'Bm', 'D', 'Em', 'F#m', 'F#', 'G', 'A'}
    C_minor = {'Cm', 'D#', 'Fm', 'Gm', 'G', 'G#', 'A#'}
    Cs_minor = {'C#m', 'E', 'F#m', 'G#m', 'G#', 'A', 'B'}
    D_minor = {'Dm', 'F', 'Gm', 'Am', 'A', 'A#', 'C'}
    Ds_minor= {'D#m', 'F#', 'G#m', 'A#m', 'A#', 'B', 'C#'}
    E_minor = {'Em', 'G', 'Am', 'Bm', 'B', 'C', 'D'}
    F_minor = {'Fm', 'G#', 'A#m', 'Cm', 'C', 'C#', 'D#'}
    Fs_minor = {'F#m', 'A', 'Bm', 'C#m', 'C#', 'D', 'E'}
    G_minor = {'Gm', 'A#', 'Cm', 'Dm', 'D', 'D#', 'F'}
    Gs_minor= {'G#m', 'B', 'C#m', 'D#m', 'D#', 'E', 'F#'}

    #targetと一致する要素のみのセットに変換
    C = target & C_Major
    Cs = target & Cs_Major
    D = target & D_Major
    Ds = target & Ds_Major
    E = target & E_Major
    F = target & F_Major
    Fs = target & Fs_Major
    G  = target & G_Major
    Gs = target & Gs_Major
    A = target & A_Major
    As = target & As_Major
    B = target & B_Major

    Am = target & A_minor
    Asm = target & As_minor
    Bm = target & B_minor
    Cm = target & C_minor
    Csm = target & Cs_minor
    Dm = target & D_minor
    Dsm = target & Ds_minor
    Em = target & E_minor
    Fm = target & F_minor
    Fsm = target & Fs_minor
    Gm = target & G_minor
    Gsm = target & Gs_minor

    #keyにキーの名前、valueに要素数を格納した辞書型リストを作成
    all = {'Cメジャー': len(C), 'C#メジャー': len(Cs), 'Dメジャー': len(D), 'D#メジャー': len(Ds), 'Eメジャー': len(E), 'Fメジャー': len(F),\
           'F#メジャー': len(Fs), 'Gメジャー': len(G), 'G#メジャー': len(Gs), 'Aメジャー': len(A), 'A#メジャー': len(As), 'Bメジャー': len(B),\
           'Aマイナー': len(Am), 'A#マイナー': len(Asm), 'Bマイナー': len(Bm), 'Cマイナー': len(Cm), 'C#マイナー': len(Csm), 'Dマイナー': len(Dm),\
           'D#マイナー': len( Dsm), 'Eマイナー': len(Em), 'Fマイナー ': len(Fm), 'F#マイナー': len(Fsm), 'Gマイナー': len(Gm), 'G#マイナー': len(Gsm)}
       
    #最も一致するコードが多いキーの名前を取得
    max_key = [key[0] for key in all.items() if key[1] == max(all.values())]

    return render_template('index.html', \
                    title = 'キーチェッカー', \
                    message = '{}の可能性が高いです。'.format(max_key))

app.run(port=8000, debug=True)
