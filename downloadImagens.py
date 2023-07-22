from bing_image_downloader import downloader

filtro = 'sam winchester'
destino = 'C:\\Users\\My\\Downloads\\YoloV4Scripts-main\\YoloV4Scripts-main\\sobrenatural\\sam\\dataset'

print('Iniciando downloads...')
try:
    downloader.download(filtro, limit=10, output_dir=destino, adult_filter_off=True, force_replace=False)

    print('Downloads concluídos!')
except Exception as e:
    print('Erro ao fazer o download:', e)