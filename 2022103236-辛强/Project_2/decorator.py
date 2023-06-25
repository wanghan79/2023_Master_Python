import MLPackage.MLmodel as models
import StandardPackage.standards as standards
import DataSamling.DataSamling as DataSamling

@DataSamling("int","float","str","tuple")
@standards("MCC", "ACC")
@models("SVM","RF","CNN","RNN")

def SentificTest(*args,**kwargs):
    #1.Create Data
    pass
    return DataSamling()

SentificTest()