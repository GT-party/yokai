import os,stat
# Список расширений для видеофайлов
video_extensions = [
    ".mp4",  # MPEG-4 Video
    ".avi",  # Audio Video Interleave
    ".mov",  # QuickTime Movie
    ".wmv",  # Windows Media Video
    ".flv",  # Flash Video
    ".mkv",  # Matroska Video
    ".webm", # WebM Video
    ".mpeg", # MPEG Video
    ".3gp",  # 3GPP Multimedia File
    ".m4v",  # MPEG-4 Video
    ".f4v",  # Flash MP4 Video
    ".ogg",  # Ogg Video
    ".ts",   # MPEG Transport Stream
]

# Список расширений для текстовых файлов
text_extensions = [
    ".txt",  # Plain Text
    ".doc",  # Microsoft Word Document
    ".docx", # Microsoft Word Open XML Document
    ".pdf",  # Portable Document Format
    ".rtf",  # Rich Text Format
    ".odt",  # OpenDocument Text Document
    ".tex",  # LaTeX Source Document
    ".html", # HyperText Markup Language
    ".xml",  # eXtensible Markup Language
    ".md",   # Markdown Document
    ".epub", # Electronic Publication
    ".csv",  # Comma-Separated Values
    ".json", # JavaScript Object Notation
]

# Список расширений для изображений
image_extensions = [
    ".jpg",  # JPEG Image
    ".jpeg", # JPEG Image
    ".png",  # Portable Network Graphics
    ".gif",  # Graphics Interchange Format
    ".bmp",  # Bitmap Image File
    ".tiff", # Tagged Image File Format
    ".svg",  # Scalable Vector Graphics
    ".webp", # WebP Image
    ".psd",  # Adobe Photoshop Document
    ".raw",  # Raw Image Format
    ".heic", # High Efficiency Image Format
    ".ico",  # Icon File
    ".ai",   # Adobe Illustrator Artwork]
]
# Аудио файлы
audio_files = [
    ".mp3",  # MPEG Audio Layer III
    ".wav",  # Waveform Audio File Format
    ".flac", # Free Lossless Audio Codec
    ".aac",  # Advanced Audio Codec
    ".ogg",  # Ogg Vorbis Audio
    ".wma",  # Windows Media Audio
    ".m4a"   # MPEG-4 Audio
]

# Архивы и сжатые файлы
compressed_files = [
    ".zip",  # ZIP Archive
    ".rar",  # RAR Archive
    ".7z",   # 7-Zip Archive
    ".tar",  # Tape Archive
    ".gz",   # Gzip Compressed Archive
    ".bz2",  # Bzip2 Compressed Archive
    ".iso"   # ISO Disc Image
]

# Исполняемые файлы
executable_files = [
    ".exe",  # Executable File
    ".bat",  # Batch File
    ".sh",   # Shell Script
    ".msi"   # Microsoft Installer Package
]

# Базы данных
database_files = [
    ".sql",   # Structured Query Language Data
    ".db",    # Database File
    ".mdb",   # Microsoft Access Database
    ".accdb"  # Microsoft Access 2007 Database
]

# Код и скрипты
code_and_scripts = [
    ".py",   # Python Script
    ".js",   # JavaScript File
    ".java", # Java Source Code
    ".c",    # C Source Code
    ".cpp",  # C++ Source Code
    ".php",  # PHP Script
    ".rb"    # Ruby Script
]

# Презентации и электронные таблицы
presentations_and_spreadsheets = [
    ".ppt",  # PowerPoint Presentation
    ".pptx", # PowerPoint Open XML Presentation
    ".xls",  # Excel Spreadsheet
    ".xlsx"  # Excel Open XML Spreadsheet
]
spreadsheet_extensions = [
    ".xls",
    ".xlsx",
    ".ods",
    ".csv",
    ".tsv",
    ".numbers",
    ".xlsm"
]
torrent_extensions = [
    ".torrent",
    ".magnet"
]



def makedir():
    path_us=str(input("Введи директорию, которую хотить сортировать: ")).replace("\\","/")
    
    os.chdir(path_us)
    os.chmod(path_us,stat.S_IRWXU)
    os.makedirs("image",exist_ok=True)
    os.makedirs("video",exist_ok=True)
    os.makedirs("text",exist_ok=True)
    os.makedirs("presentations",exist_ok=True)
    os.makedirs("audio",exist_ok=True)
    os.makedirs("zip",exist_ok=True)
    os.makedirs("programs",exist_ok=True)
    os.makedirs("database",exist_ok=True)
    os.makedirs("code",exist_ok=True)
    os.makedirs("torrent",exist_ok=True)
    os.makedirs("spreadsheet",exist_ok=True)
 




def sort():
    for papk in os.listdir():
        try:
            file_name,file_path = os.path.splitext(papk)
            if file_path in video_extensions:
                os.replace(papk, os.path.join('video', papk))

            elif file_path in image_extensions:
                os.replace(papk, os.path.join('image', papk))

            elif file_path in text_extensions:
                os.replace(papk, os.path.join('text', papk))

            elif file_path in presentations_and_spreadsheets:
                os.replace(papk, os.path.join('presentations', papk))

            elif file_path in audio_files:
                os.replace(papk, os.path.join('audio', papk))

            elif file_path in compressed_files:
                os.replace(papk, os.path.join('zip', papk))

            elif file_path in executable_files:
                os.replace(papk, os.path.join('programs', papk))

            elif file_path in database_files:
                os.replace(papk, os.path.join('database', papk))

            elif file_path in code_and_scripts:
                os.replace(papk, os.path.join('code', papk))
            
            elif file_path in spreadsheet_extensions:
                os.replace(papk, os.path.join('spreadsheet', papk))

            elif file_path in torrent_extensions:
                os.replace(papk, os.path.join('torrent', papk))

            
        except Exception as e:
                print(f"Ошибка переноса файла: {papk}: {e}")
                break
    print("Файлы отсортированы")
    

makedir()
sort()