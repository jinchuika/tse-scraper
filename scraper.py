import os
import json
import numpy as np
import asyncio
import concurrent.futures
import requests
import shutil

url = 'https://resultados2019.tse.org.gt/201901/api.php'

# obtén tu propio token desde la página del TSE
token = ''
# la carpeta donde desees guardar los datos
output_folder_raw = ''
# la carpeta donde quieras guardar las imágenes
# dentro de esta carpeta debes generar otras 5 llamadas 0, 1, 2, 3, y 4
output_folder_images = ''


def query_api(num):
    params = {'token': token, 'mesa': num, 'vista': 'MESA'}
    query_url = f'{url}?token={params["token"]}&mesa={params["mesa"]}&vista={params["vista"]}'
    print(f'Consulting... : {num}')
    r = requests.get(url=query_url, data=params)
    data = r.json()
    with open(f'{output_folder_raw}/{num}.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
    try:
        for i, te in enumerate(data['TE']):
            folder = f'{output_folder_images}/{i}'
            extension = te['IMGSRC'].split('.')[-1]
            if f'{num}.{extension}' not in os.listdir(folder):
                response = requests.get(te['IMGSRC'], stream=True)
                with open(f'{output_folder_images}/{i}/{num}.{extension}', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
    except KeyError:
        pass
    print(f'Done with {num}')


async def main():
    starting = 1
    ending = 21100
    excluded = [int(f.replace('.json', '')) for f in os.listdir(output_folder_raw)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                query_api,
                i
            )
            for i in np.setdiff1d([i for i in range(starting, ending)], excluded)
        ]
        for response in await asyncio.gather(*futures):
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
