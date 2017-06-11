import numpy as np
import SimpleITK as sitk

_patientInfoDictKey = "JPatientInformation"
_mriDeviceDictKey = "JMRIDeviceInfo"
_sessionNameKey = "JSessionNameKey"
class _Session:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        if self.path != None:
            _file = sitk.ReadImage(self.path)
            header_keys = _file.GetMetaDataKeys()
            for key in header_keys:
                # patient info
                if key.__contains__(_patientInfoDictKey):
                    dict_key = key.replace(_patientInfoDictKey,"")
                    self.patient_info[dict_key] = _file.GetMetaData(key)
                # MRI device info
                elif key.__contains__(_mriDeviceDictKey):
                    dict_key = key.replace(_mriDeviceDictKey, "")
                    self.mri_device_info[dict_key] = _file.GetMetaData(key)
                elif key.__contains__(_sessionNameKey):
                    self.name = _file.GetMetaData(key)
            self.image = sitk.GetArrayFromImage(_file)

    name = ""
    patient_info = {}
    mri_device_info = {}
    image = np.zeros(0)
    path = None
    pass

def open_session(path=None):
    if path == None:
        return
    s = _Session(path=path)
    return s

def close_session(session=None):
    return