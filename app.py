from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# --- DATABASE DENGAN MINIMAL 5 PILIHAN FILM & MUSIK POPULER ---
DATABASE_REKOMENDASI = {
    "burnout": {
        "status": "🔥 Stres & Overwhelmed (Burnout)",
        "kegiatan": "🧘 Lakukan teknik pernapasan kotak (box breathing) selama 5 menit atau tuliskan keluh kesahmu di selembar kertas (Brain Dump).",
        "film": [
            {"judul": "Soul (Pixar)", "pesan": "mengingatkan kita untuk menikmati setiap detik hal kecil di hidup tanpa terbeban ambisi."},
            {"judul": "Freedom Writers", "pesan": "melihat kisah nyata bagaimana ketulusan menulis bisa mengurai tumpukan beban mental."},
            {"judul": "The Secret Life of Walter Mitty", "pesan": "mengajarkan kita untuk berani keluar dari rutinitas yang menjemukan dan mulai menikmati hidup."},
            {"judul": "Little Miss Sunshine", "pesan": "kisah keluarga unik yang mengajarkan bahwa gagal atau lelah itu manusiawi, yang penting tetap bersama."},
            {"judul": "Eat Pray Love", "pesan": "menemukan kembali kedamaian diri dan menyembuhkan lelah batin akibat tekanan hidup yang berat."}
        ],
        "musik": [
            "🌧️ Audio Terapi Alam (Suara kombinasi Hujan & Ombak penurun detak jantung)",
            "🎹 Weightless - Marconi Union (Musik instrumental terpopuler untuk meredakan cemas)",
            "🎻 Cozy Instrumental Piano Playlist (Alunan piano lembut penenang pikiran)",
            "🌲 Forest Ambience & Bird Chirping (Suara hutan dan burung pelipur stres)",
            "🌌 Deep Sleep & Anti-Anxiety Lofi Beats (Ritme ketukan santai pengurai kepanikan)"
        ]
    },
    "lost": {
        "status": "🧭 Kehilangan Arah / Kurang Motivasi (Lost)",
        "kegiatan": "📝 Rapikan meja belajarmu, lalu tulis 1 target paling kecil yang bisa kamu selesaikan dalam 10 menit ke depan.",
        "film": [
            {"judul": "Laskar Pelangi", "pesan": "melihat keterbatasan fasilitas yang justru melahirkan mimpi besar yang mengguncang dunia."},
            {"judul": "The Pursuit of Happyness", "pesan": "menyaksikan perjuangan pantang menyerah yang akan membakar kembali motivasimu."},
            {"judul": "Negeri 5 Menara", "pesan": "menanamkan tekad kuat lewat mantra 'Man Jadda Wajada'—siapa yang bersungguh-sungguh pasti berhasil."},
            {"judul": "Forrest Gump", "pesan": "menginspirasi kita untuk terus melangkah maju dengan jujur tanpa perlu mencemaskan masa depan."},
            {"judul": "Dead Poets Society", "pesan": "membangkitkan kecintaan belajar secara merdeka dan menemukan jati diri yang sesungguhnya."}
        ],
        "musik": [
            "🎤 Playlist Lagu Semangat Populer (Contoh: Manusia - Tulus)",
            "🔥 J-Pop Anime Openings (Instrumental bersemangat pembakar jiwa juang)",
            "🎸 Akustik Indie-Pop Uplifting (Lagu bernada ceria yang memicu hormon dopamin)",
            "🛹 Lo-Fi Hip Hop Workout Energy (Ketukan konstan pembawa aura produktif)",
            "🔊 Epic Cinematic Instrumental (Musik megah penggugah tekad dan ambisi)"
        ]
    },
    "fatigue": {
        "status": "💤 Lelah Mental / Sulit Fokus (Fatigue)",
        "kegiatan": "🚶 Pijat pelipis mata yang lelah, cuci muka dengan air dingin, atau lakukan peregangan otot ringan selama 3 menit.",
        "film": [
            {"judul": "3 Idiots", "pesan": "komedi cerdas seputar dunia pendidikan yang dijamin bikin kamu tertawa sekaligus melek."},
            {"judul": "Spider-Man: Into the Spider-Verse", "pesan": "animasi beritme cepat dan penuh warna yang sangat ampuh menyegarkan mata layu."},
            {"judul": "Life of Pi", "pesan": "menyajikan petualangan visual bertahan hidup yang memukau agar rasa kantukmu hilang."},
            {"judul": "Interstellar", "pesan": "mengajak otakmu berpikir tentang konsep sains ruang angkasa yang seru agar tidak mengantuk."},
            {"judul": "Zootopia", "pesan": "animasi komedi investigasi yang seru, segar, dan berenergi tinggi untuk mengusir lelah."}
        ],
        "musik": [
            "🎻 Musik Klasik Efek Mozart (Terbukti menstimulasi fokus dan konsentrasi)",
            "🧠 Deep Focus Alpha Waves (Gelombang suara khusus penahan kantuk saat belajar)",
            "☕ Coffee Shop Instrumental Jazz (Nuansa kafe yang bikin otak rileks tapi tetap terjaga)",
            "🎹 Studio Ghibli Piano Cover Playlist (Kompilasi melodi yang menyegarkan pikiran penat)",
            "⚡ Synthwave / Retrowave Beats (Tempo elektrik yang stabil untuk menjaga mata tetap melek)"
        ]
    }
}

@app.route('/api/hitung-mood', methods=['POST'])
def hitung_mood():
    data = request.get_json()
    jawaban = data.get('jawaban', [])
    
    count_1 = jawaban.count(1)
    count_2 = jawaban.count(2)
    count_3 = jawaban.count(3)
    
    if count_1 >= count_2 and count_1 >= count_3:
        kategori = "burnout"
    elif count_2 >= count_1 and count_2 >= count_3:
        kategori = "lost"
    else:
        kategori = "fatigue"
        
    data_mood = DATABASE_REKOMENDASI[kategori]
    
    # Python memilih secara acak 1 dari 5 pilihan yang sekarang sudah tersedia
    film_terpilih = random.choice(data_mood["film"])
    musik_terpilih = random.choice(data_mood["musik"])
    
    html_response = f"""
    <div class="text-center mb-4">
        <span class="px-3 py-1 bg-gradient-to-r from-cyan-500/10 to-blue-500/10 text-cyan-400 border border-cyan-500/20 rounded-full text-xs font-semibold uppercase tracking-wider">Hasil Analisis Psikologi Python</span>
        <h4 class="text-xl font-bold text-white mt-2">Kondisimu: <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-teal-400 font-extrabold">{data_mood['status']}</span></h4>
    </div>
    <hr class="border-gray-800 my-4">
    
    <div class="space-y-4">
        <div class="p-4 bg-white/5 rounded-xl border border-gray-800/60">
            <p class="text-cyan-400 font-bold text-xs uppercase tracking-wider mb-1">🎬 Tontonan Rekomendasi:</p>
            <p class="text-gray-200 text-sm">Film <strong>"{film_terpilih['judul']}"</strong> — {film_terpilih['pesan']}</p>
        </div>
        
        <div class="p-4 bg-white/5 rounded-xl border border-gray-800/60">
            <p class="text-teal-400 font-bold text-xs uppercase tracking-wider mb-1">🎧 Audio Rekomendasi:</p>
            <p class="text-gray-200 text-sm">{musik_terpilih}</p>
        </div>
        
        <div class="p-4 bg-emerald-500/5 rounded-xl border border-emerald-500/20">
            <p class="text-yellow-400 font-bold text-xs uppercase tracking-wider mb-1">🏃 Kegiatan Penyegar (Refreshing):</p>
            <p class="text-gray-300 text-sm leading-relaxed">{data_mood['kegiatan']}</p>
        </div>
    </div>
    """

    return jsonify({"result_html": html_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)