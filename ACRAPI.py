from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType
from SongIDCore import *




# Get the ACRCloud config
with open('data/acrcloud.json', 'r') as f:
    config = json.load(f)
    logger.info('Loaded: ACR Config')

config_clear = config["clear"]
config_clear["access_key"] = os.environ.get('songid_acr_clear_key')
config_clear["access_secret"] = os.environ.get('songid_acr_clear_secret')
config_clear["recognize_type"] = ACRCloudRecognizeType.ACR_OPT_REC_AUDIO
config_clear["debug"] = False


config_noisy = config["noisy"]
config_noisy["access_key"] = os.environ.get('songid_acr_noisy_key')
config_noisy["access_secret"] = os.environ.get('songid_acr_noisy_secret')
config_noisy["recognize_type"] = ACRCloudRecognizeType.ACR_OPT_REC_AUDIO
config_noisy["debug"] = False


config_hum = config["hum"]
config_hum["access_key"] = os.environ.get('songid_acr_hum_key')
config_hum["access_secret"] = os.environ.get('songid_acr_hum_secret')
config_hum["recognize_type"] = ACRCloudRecognizeType.ACR_OPT_REC_BOTH
config_hum["debug"] = False



# Functions for sending files to the ACRCloud API and getting a response
# These functions were pre-made on the ACRCloud GitHub: https://github.com/acrcloud/acrcloud_sdk_python/blob/master/windows/win64/python3/test.py
class ACRAPI():
    #def clear(filePath):
    # Not currently using clear-audio detection, so the function is not necessary




    def noisy(filePath):
        config = config_noisy

        '''This module can recognize ACRCloud by most of audio/video file.
            Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
            Video: mp4, mkv, wmv, flv, ts, avi ...'''
        re = ACRCloudRecognizer(config)

        #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
        #re.recognize_by_file(filePath, 0, 10)
        logger.info('ACR: Processing request...')
        buf = open(filePath, 'rb').read()
        #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
        data = re.recognize_by_filebuffer(buf, 0, 60)
        data = json.loads(data)
        logger.info('ACR: Processing complete!')
        return data




    def hum(filePath):
        config = config_hum

        '''This module can recognize ACRCloud by most of audio/video file.
            Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
            Video: mp4, mkv, wmv, flv, ts, avi ...'''
        re = ACRCloudRecognizer(config)

        #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
        #re.recognize_by_file(filePath, 0, 10)
        logger.info('ACR: Processing request...')
        buf = open(filePath, 'rb').read()
        #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
        data = re.recognize_by_filebuffer(buf, 0, 10)
        data = json.loads(data)
        logger.info('ACR: Processing complete!')
        return data