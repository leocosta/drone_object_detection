import requests
import os.path

CONFIG = {
    "yolov3-tiny": [
        {
            "origin": "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny.cfg",
            "destination": "yolo-coco/yolov3-tiny.cfg"
        },
        {
            "origin": "https://pjreddie.com/media/files/yolov3-tiny.weights",
            "destination": "yolo-coco/yolov3-tiny.weights"
        }
    ],
    "yolov3": [
        {
            "origin": "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3.cfg",
            "destination": "yolo-coco/yolov3.cfg"
        },
        {
            "origin": "https://pjreddie.com/media/files/yolov3.weights",
            "destination": "yolo-coco/yolov3.weights"
        }
    ]
}

def download_assets(version):

    files = []
    if version in CONFIG:
        files = CONFIG[version]
    else:
        raise ValueError("Versão inválida: {}.".format(version))

    for file in list(files):
        origin_file = file["origin"]
        destination_file = file["destination"]

        if not os.path.exists(destination_file):
            download_file(origin_file, destination_file)
        else:
            print("[+] Arquivo {} já foi baixado.".format(destination_file))

def download_file(origin_file, destination_file):
    with open(destination_file, "wb") as f:
            response = requests.get(origin_file, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = (dl / total_length) * 100.
                    print("[+] Baixando {0}: {1:.2f}%".format(destination_file, done))