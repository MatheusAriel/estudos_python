import qrcode

# Seu texto grande
texto_grande = """
C.E.M.E.I Cônego 
Manoel Tobias
Rua Major Manoel Antônio de Mattos, 
1561 - Vila Nery
Instituto De Educação Dr. Álvaro Guião
E.E. Prof. Luiz Augusto De Oliveira
ETEC Paulino Botelho
Fundação Educacional De São Carlos
E.E. Prof. José Juliano Neto
E.E. Cel. Paulino Carlos
E.E. Antônio Militão De Lima
C.E.M.E.I Cônego Manoel Tobias
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
215, 228, 233, 272, 314, 326, 339, 67, 
68, 69, 70, 71, 72, 73, 74, 75, 76, 227, 
270, 280, 98, 99, 100, 101, 102,103, 
104, 105, 106, 107, 108, 236, 267, 308, 
282, 297, 325, 398, 152, 153, 154, 155, 
156, 157, 158, 159, 160, 221, 222, 275, 
289, 305, 347, 27, 28, 29, 30, 31, 32, 
33, 34, 35, 36, 271, 129, 130, 131, 132, 
133, 134, 135, 136, 137, 138, 240, 329, 
345, 373, 388
C.E.M.E.I Aracy Leite 
P. Lopes
Rua Dr. Carlos Camargo Salles, 163 - Jd. 
Lutfalla 
E.E. Prof. Sebastião De Oliveira Rocha
Escola De Engenharia De São Carlos - U.S.P.
77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 
230, 269, 298, 336, 109, 110, 111, 112, 
113, 114, 115, 116, 117, 118, 237, 247, 
266, 286, 294,302, 309, 318, 324, 332, 
338, 354, 360, 369, 379, 403, 432, 442
C.E.M.E.I Walter 
Blanco
Rua Francisco Gentil de Guzzi, 135 - 
Santa Felícia
E.E. Conde Do Pinhal
E.M.E.B Angelina Dagnone De Melo
174, 177, 187, 188, 189, 190, 191, 
192,194, 195, 216, 234, 327, 364, 371, 
375/439, 381, 386, 389, 397, 406, 412, 
419, 427, 439
C.E.M.E.I. Prof. 
Vicente De Paulo 
Rocha Keppe
Rua Miguel Fucci, 50 - Santa Felícia E.E. Profa. Attilia Prado Margarido
C.E.M.E.I Vicente De Paulo Rocha Keppe
246, 249, 256, 257, 259, 262, 264, 283, 
288, 292, 307, 319, 328, 429, 342, 355, 
363, 370, 376, 380, 387, 391
C.E.M.E.I. Deputado 
Vicente Botta Rua Otto Werner Rosel, 90 - Jd. Ipanema 
C.E.M.E.I. - Maria Luiza Peres
E.E. Bento Da Silva Cesar
UNICEP - Centro Universitário Central 
Paulista
352, 366, 390, 433, 279, 285, 293, 299, 
304, 313, 323, 330, 337, 346, 349, 358, 
424, 394, 401, 404, 408, 411, 414, 416, 
423, 426, 428, 430, 435, 437, 443
E.M.E.B Maria 
Ermantina C. Tarpani 
Rua João Pedrino, nº 100, Jardim 
Botafogo
E.E. Prof. Gabriel Felix Do Amaral
E.M.E.B. Maria Ermantina Carvalho Tarpani
38, 127, 134, 153, 167, 182, 199, 218, 
236, 250, 283, 287, 301, 311
E.M.E.B Carmine 
Botta Rua Philomena Fauvel, s/n° - Bela Vista E.E. Prof. Elydia Benetti
E.M.E.B. Carmine Botta
66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 
77, 176, 185, 193, 203, 215, 224, 230, 
242, 262, 275, 288, 299
C.E.M.E.I. Carmelita 
Rocha Ramalho Avenida Sallum, 685 - Vila Prado 
E.E. Eugenio Franco
E.E. Prof. Maria Ramos
E.E. Bispo Dom Gastão
Centro Educacional Diocesano La Salle
C.E.M.E.I. Carmelita Rocha Ramalho
88, 89, 90, 91, 92, 96, 97, 98, 28, 125, 
130, 132. 149, 156, 161, 168, 173, 265, 
56, 57, 58, 59, 60, 61, 64, 65, 146, 99, 
100, 101, 102, 103, 104, 105, 106, 107, 
108, 221, 237, 142, 157, 166, 177, 187, 
202, 227, 257, 269
C.E.M.E.I. Prof. João 
Jorge Marmorato Rua Santa Gertrudes, 475 – Vila Isabel 
E.E. Prof. João Jorge Marmorato
E.E. Prof. Antônio Adolfo Lobbe
Sesi Serviço Social Industria
E.E. Prof. Arlindo Bittencourt
C.E.M.E.I. Lauro Monteiro Cruz
E.E. Jesuino De Arruda
123, 135, 155, 171, 186, 208, 234, 270, 
290, 335, 30, 32, 33, 34, 35, 36, 37, 181, 
210, 231, 245, 285, 304, 331, 42, 43, 44, 
45, 46, 47, 48, 49, 50, 51, 52, 53, 226, 
233, 255, 286, 312, 140, 154, 165, 180, 
191, 204, 111, 112, 113, 114, 115, 116, 
117, 118, 120, 121, 122, 188, 195, 212, 
228, 259, 274, 293, 340
[23/8 18:38] João: C.E.M.E.I Dr. João 
Baptista Paino Rua Aristides de Santi, 187 - Azulville C.E.M.E.I. João Baptista Paino 323, 327
Centro da Juventude 
Elaine Viviani Rua Paulo VI, 1000 – Jardim Monte Carlo E.E. Pericles Soares
E.E. Dona Aracy Leite Pereira Lopes
175, 194, 238, 251, 267, 292, 78, 79, 80, 
81, 82, 83, 84, 85, 86, 170, 189, 206
E.M.E.B Prof. Afonso 
Fioca Vitali (CAIC) Rua Regit Arab, s/n° - Cidade Aracy
E.M.E.B. Prof. Afonso Fioca Vitali (CAIC)
E.E. Prof. Orlando Perez
E.E. Prof. Ary Pinto Das Neves
39, 40, 41, 126, 128, 131, 136, 147, 162, 
183, 196, 211, 219, 232, 244, 249, 260, 
266, 276, 289, 310, 139, 148, 150, 159, 
169, 178, 190, 200, 209, 216, 268, 284, 
297, 324, 296, 298
E.M.E.B Arthur 
Natalino Deriggi
Rua José Francisco Bicaletto, 13 - Cidade 
Aracy E.M.E.B Arthur Natalino Deriggi 220, 239, 252, 263, 273, 281, 291, 295, 
302, 306, 314, 330, 338, 343
C.E.M.E.I Renato 
Jensem 
Rua Dorovaldo Rodrigues, 575 - Res. Dep. 
José Zavaglia
E.E. Prof. João Batista Gasparin (E.E. Jd. 
Zavaglia) 322, 325
E.M.E.B Prof. Antonio 
Stella Moruzzi Rua Teotônio Vilela, 501 - Jardim Tangará E.M.E.B Prof. Antonio Stella Moruzzi 341, 359, 368, 382, 385, 396, 409, 
418, 438
C.E.M.E.I. Antônio De 
Lourdes Rondon
Rua Olavo Zabotto, 105 - Maria Stella 
Faga 
Centro Educacional Sesi n. 108
E.E. Prof. Archimedes Aristeu Mendes De 
Carvalho
C.E.M.E.I. Antônio De Lourdes Rondon
393, 400, 407, 413, 425, 436, 252, 258, 
263, 284, 290, 301, 306, 315, 322, 331, 
344, 356, 365, 374, 384
C.E.M.E.I Profª Marli 
de Fátima Alves
Rua Bento da Silva César, 101 - Santa 
Maria II E.E. Marilene Terezinha Longhin 278, 291, 310, 335, 362
C.E.M.E.I Helena 
Dornfeld
Rua Estados Unidos, 1181 – Vila Costa 
do Sol
E.E. Esterina Placco
E.E. Prof. Andrelino Vieira
C.E.M.E.I. Helena Dornfeld
Colégio Cecília Meirelles
88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 
217, 232, 260, 268, 300, 311, 321, 333, 
196, 197, 198, 199, 200, 201, 274, 340, 
351, 372, 378, 392, 440, 277, 296, 316, 
353, 399
E.M.E.B Profª Dalila 
Galli Rua Rio Araguaia, s/n° - Jockey Club
E.M.E.B. Dalila Galli
Universidade Federal De São Carlos
E.E. Prof. Ludgero Braga
343, 357, 367, 377, 395, 410, 417, 434, 
281, 320, 361, 383, 402, 415, 431, 441, 
244, 255, 261, 273, 287, 295, 303, 317
C.E.M.E.I Santo Piccin Avenida Bela Cintra, s/n° - Água Vermelha E.E. Adail M. Gonçalves 141, 142, 276, 312, 348, 405
C.E.M.E.I José de Brito Castro Rua Rui Barbosa, s/n° - Santa Eudóxia E.E. Visconde Cunha Bueno 139, 140, 210, 265, 334, 350
"""

# Crie um objeto QRCode com o texto grande
qr = qrcode.QRCode(
    version=40,  # A versão do QR code (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro (L, M, Q, H)
    box_size=10,  # Tamanho de cada "caixa" do QR code
    border=4,     # Margem ao redor do QR code
)

# Adicione os dados ao QR code
qr.add_data(texto_grande)
qr.make(fit=False)

# Crie uma imagem do QR code usando a biblioteca PIL (Python Imaging Library)
qr_code_img = qr.make_image(fill_color="black", back_color="white")

# Salve a imagem do QR code
qr_code_img.save("locais_de_votacao.png")
