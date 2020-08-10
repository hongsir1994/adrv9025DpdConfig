#################################################################################
#GUI Version: 0.0.0.200
#DLL Version: 0.0.0.188
#Cmd Server Version: 0.0.0.188
#FPGA Version: 0xC900000F
#ARM Version: 0.0.0.110(ADI_ADRV9010_ARMBUILD_TESTOBJ)
#StreamVersion: 0.0.0.28
#################################################################################

#Import Reference to the DLL
import System
import clr
import time
from System import Array
clr.AddReferenceToFileAndPath("C:\\Program Files\\Analog Devices\\ADRV9025 Transceiver Evaluation Software_x64_FULL\\adrvtrx_dll.dll")
from adrv9010_dll import AdiEvaluationSystem
from adrv9010_dll import Types
from adrv9010_dll import Ad9528Types
from math import log10, sqrt
def resetDpdFull(TxChannel):#reset 只需要使用通道号就可以使用,相应的函数
    if TxChannel == 1:
        link.platform.board.Adrv9010Device.Dfe.DpdReset(Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX1,Types.adi_adrv9010_DpdResetMode_e.ADI_ADRV9010_DPD_RESET_FULL)
    if TxChannel == 2:
        link.platform.board.Adrv9010Device.Dfe.DpdReset(Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX2,Types.adi_adrv9010_DpdResetMode_e.ADI_ADRV9010_DPD_RESET_FULL)
    if TxChannel == 3:
        link.platform.board.Adrv9010Device.Dfe.DpdReset(Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX3,Types.adi_adrv9010_DpdResetMode_e.ADI_ADRV9010_DPD_RESET_FULL)
    if TxChannel == 4:
        link.platform.board.Adrv9010Device.Dfe.DpdReset(Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX4,Types.adi_adrv9010_DpdResetMode_e.ADI_ADRV9010_DPD_RESET_FULL)

def spiRead(address):
    data = adrv9010.Hal.SpiByteRead(address, 0)
    print "SPI Read Address " + hex(address) + ": " + hex(data[1])

def spiWrite(address, data):
    adrv9010.Hal.SpiByteWrite(address, data)
    print "SPI Write Address " + hex(address) + ": " + hex(data)


luts = {
    0:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0,
    1:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT1,
    2:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT2,
    3:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT3,
    4:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT4,
    5:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT5,
    6:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT6,
    7:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT7,
    8:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8,
    9:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT9,
    10:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT10,
    11:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT11,
    12:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT12,
    13:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT13,
    14:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT14,
    15:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT15,
    16:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT16,
    17:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT17,
    18:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT18,
    19:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT19,
    20:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT20,
    21:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT21,
    22:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT22,
    23:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT23,
    24:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT24,
    25:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT25,
    26:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT26,
    27:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT27,
    28:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT28,
    29:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT29,
    30:Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT30
    }

TxCh = Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX2 # ()why set to Tx2, question by feigo/需要设置相关的通道2
intDpdLut =Types.adi_adrv9010_DpdLut_e
intDpdModelSel = Types.adi_adrv9010_DpdModelSel_e
intDpdActCompSize = Types.adi_adrv9010_DpdActuatorCompanderSize_e
intDpdResetMode = Types.adi_adrv9010_DpdResetMode_e
intDpdErr = Types.adi_adrv9010_DpdError_e
intDpdStatus = Types.adi_adrv9010_DpdStatus_t
intDpdModel = Types.adi_adrv9010_DpdModelConfig_t

def dpdModelConfigSet():
    dpdModel = Types.adi_adrv9025_DpdModelConfig_t()
    #retVal = link.platform.board.Adrv9010Device.Dfe.DpdModelConfigGet(TxCh, dpdModel)
    #dpdModel = retVal[1]
   
    #读取先关的参数进行设置
    f = open(r"C:\Users\fzhang2\OneDrive - Analog Devices, Inc\Documents\MaduraDPD\Mudra95Coe.txt", 'r')
    #f = open("C:\\Corwin\\Madura\\8T8R\\Mudra95Coe.txt", 'r')
    #f = open("E:\\Transceivers\\Tokelau\\CustomerIssues\\Nokia\\NokiaNaperville\\Dpd_PATesting\\testModelNew63_FinalOpt.txt", 'r')

    rows = f.readlines() #记录所有行的信息
    f.close()
    n = 0
    for row in rows:
        row = row.strip()
        #print row
        if row == '':
            continue
        if row[0] == '/':
            continue  
        row = row.split()
        #print row
        dpdModel.dpdFeatures[n].i = int(row[0]) #读取和需要设置的参数,读取第一行的第一个参数,一下一次类推
        #print int(row[0])
        dpdModel.dpdFeatures[n].j = int(row[1])
        dpdModel.dpdFeatures[n].k = int(row[2])
        dpdModel.dpdFeatures[n].lut = luts[int(row[3])]
        #print luts[int(row[3])]
        dpdModel.dpdFeatures[n].coeffReal = float(row[4])
        dpdModel.dpdFeatures[n].coeffImaginary = float(row[5])
        n = n + 1
            
    dpdModel.dpdNumFeatures = n
    print 'Number of Coefficients = ' + str(n)
    #dpdModel.dpdModelIndex = Types.adi_adrv9010_DpdModelSel_e.ADI_ADRV9010_DPD_MODEL0
    #dpdModel.dpdCompanderSize = Types.adi_adrv9010_DpdActuatorCompanderSize_e.ADI_ADRV9010_DPD_ACT_COMPANDER_8_BITS
    link.platform.board.Adrv9010Device.Dfe.DpdModelConfigSet(dpdModel)#作为整个结构写入到dpdconfig中

def defaultDpdModel():

    dpdModelConfigSet = Types.adi_adrv9010_DpdModelConfig_t()
    dpdModelConfigSet.dpdCompanderSize = Types.adi_adrv9010_DpdActuatorCompanderSize_e.ADI_ADRV9010_DPD_ACT_COMPANDER_8_BITS
    dpdModelConfigSet.dpdModelIndex = Types.adi_adrv9010_DpdModelSel_e.ADI_ADRV9010_DPD_MODEL0;
    dpdModelConfigSet.dpdNumFeatures = 22;

    dpdModelConfigSet.dpdFeatures[0].i = 0;
    dpdModelConfigSet.dpdFeatures[0].j = 0;
    dpdModelConfigSet.dpdFeatures[0].k = 0;
    dpdModelConfigSet.dpdFeatures[0].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0;
    dpdModelConfigSet.dpdFeatures[0].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[0].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[1].i = 0;
    dpdModelConfigSet.dpdFeatures[1].j = 0;
    dpdModelConfigSet.dpdFeatures[1].k = 1;
    dpdModelConfigSet.dpdFeatures[1].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0;
    dpdModelConfigSet.dpdFeatures[1].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[1].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[2].i = 0;
    dpdModelConfigSet.dpdFeatures[2].j = 0;
    dpdModelConfigSet.dpdFeatures[2].k = 2;
    dpdModelConfigSet.dpdFeatures[2].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0;
    dpdModelConfigSet.dpdFeatures[2].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[2].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[3].i = 0;
    dpdModelConfigSet.dpdFeatures[3].j = 0;
    dpdModelConfigSet.dpdFeatures[3].k = 3;
    dpdModelConfigSet.dpdFeatures[3].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0;
    dpdModelConfigSet.dpdFeatures[3].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[3].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[4].i = 0;
    dpdModelConfigSet.dpdFeatures[4].j = 0;
    dpdModelConfigSet.dpdFeatures[4].k = 4;
    dpdModelConfigSet.dpdFeatures[4].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0;
    dpdModelConfigSet.dpdFeatures[4].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[4].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[5].i = 0;
    dpdModelConfigSet.dpdFeatures[5].j = 0;
    dpdModelConfigSet.dpdFeatures[5].k = 8;
    dpdModelConfigSet.dpdFeatures[5].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT0;
    dpdModelConfigSet.dpdFeatures[5].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[5].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[6].i = 1;
    dpdModelConfigSet.dpdFeatures[6].j = 0;
    dpdModelConfigSet.dpdFeatures[6].k = 0;
    dpdModelConfigSet.dpdFeatures[6].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT1;
    dpdModelConfigSet.dpdFeatures[6].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[6].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[7].i = 1;
    dpdModelConfigSet.dpdFeatures[7].j = 0;
    dpdModelConfigSet.dpdFeatures[7].k = 1;
    dpdModelConfigSet.dpdFeatures[7].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT1;
    dpdModelConfigSet.dpdFeatures[7].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[7].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[8].i = 1;
    dpdModelConfigSet.dpdFeatures[8].j = 0;
    dpdModelConfigSet.dpdFeatures[8].k = 2;
    dpdModelConfigSet.dpdFeatures[8].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT1;
    dpdModelConfigSet.dpdFeatures[8].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[8].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[9].i = 1;
    dpdModelConfigSet.dpdFeatures[9].j = 0;
    dpdModelConfigSet.dpdFeatures[9].k = 3;
    dpdModelConfigSet.dpdFeatures[9].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT1;
    dpdModelConfigSet.dpdFeatures[9].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[9].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[10].i = 1;
    dpdModelConfigSet.dpdFeatures[10].j = 0;
    dpdModelConfigSet.dpdFeatures[10].k = 4;
    dpdModelConfigSet.dpdFeatures[10].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT1;
    dpdModelConfigSet.dpdFeatures[10].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[10].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[11].i = 0;
    dpdModelConfigSet.dpdFeatures[11].j = 1;
    dpdModelConfigSet.dpdFeatures[11].k = 0;
    dpdModelConfigSet.dpdFeatures[11].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8;
    dpdModelConfigSet.dpdFeatures[11].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[11].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[12].i = 0;
    dpdModelConfigSet.dpdFeatures[12].j = 1;
    dpdModelConfigSet.dpdFeatures[12].k = 1;
    dpdModelConfigSet.dpdFeatures[12].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8;
    dpdModelConfigSet.dpdFeatures[12].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[12].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[13].i = 0;
    dpdModelConfigSet.dpdFeatures[13].j = 1;
    dpdModelConfigSet.dpdFeatures[13].k = 2;
    dpdModelConfigSet.dpdFeatures[13].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8;
    dpdModelConfigSet.dpdFeatures[13].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[13].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[14].i = 0;
    dpdModelConfigSet.dpdFeatures[14].j = 1;
    dpdModelConfigSet.dpdFeatures[14].k = 3;
    dpdModelConfigSet.dpdFeatures[14].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8;
    dpdModelConfigSet.dpdFeatures[14].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[14].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[15].i = 0;
    dpdModelConfigSet.dpdFeatures[15].j = 1;
    dpdModelConfigSet.dpdFeatures[15].k = 4;
    dpdModelConfigSet.dpdFeatures[15].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8;
    dpdModelConfigSet.dpdFeatures[15].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[15].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[16].i = 0;
    dpdModelConfigSet.dpdFeatures[16].j = 1;
    dpdModelConfigSet.dpdFeatures[16].k = 5;
    dpdModelConfigSet.dpdFeatures[16].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT8;
    dpdModelConfigSet.dpdFeatures[16].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[16].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[17].i = 1;
    dpdModelConfigSet.dpdFeatures[17].j = 1;
    dpdModelConfigSet.dpdFeatures[17].k = 1;
    dpdModelConfigSet.dpdFeatures[17].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT9;
    dpdModelConfigSet.dpdFeatures[17].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[17].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[18].i = 1;
    dpdModelConfigSet.dpdFeatures[18].j = 1;
    dpdModelConfigSet.dpdFeatures[18].k = 2;
    dpdModelConfigSet.dpdFeatures[18].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT9;
    dpdModelConfigSet.dpdFeatures[18].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[18].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[19].i = 1;
    dpdModelConfigSet.dpdFeatures[19].j = 1;
    dpdModelConfigSet.dpdFeatures[19].k = 3;
    dpdModelConfigSet.dpdFeatures[19].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT9;
    dpdModelConfigSet.dpdFeatures[19].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[19].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[20].i = 1;
    dpdModelConfigSet.dpdFeatures[20].j = 1;
    dpdModelConfigSet.dpdFeatures[20].k = 4;
    dpdModelConfigSet.dpdFeatures[20].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT9;
    dpdModelConfigSet.dpdFeatures[20].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[20].coeffImaginary = 0.0;

    dpdModelConfigSet.dpdFeatures[21].i = 1;
    dpdModelConfigSet.dpdFeatures[21].j = 1;
    dpdModelConfigSet.dpdFeatures[21].k = 5;
    dpdModelConfigSet.dpdFeatures[21].lut = Types.adi_adrv9010_DpdLut_e.ADI_ADRV9010_DPD_LUT9;
    dpdModelConfigSet.dpdFeatures[21].coeffReal = 0.0;
    dpdModelConfigSet.dpdFeatures[21].coeffImaginary = 0.0;
    link.platform.board.Adrv9010Device.Dfe.DpdModelConfigSet(dpdModelConfigSet)

def dpdIndirectEvmStabilityConfigSet(txChannelMask = 0x0F): #设置相应的通道掩码
    print"***************************************"
    print"Setting up Indirect EVM Fault Condition and Recovery Action"    
    # Setup the indirect EVM fault condition
    INDIRECT_EVM_THRESH0_PERCENTAGE = 100 #Lower Threshold
    INDIRECT_EVM_THRESH1_PERCENTAGE = 100 #Upper Threshold
    ERROR_PERSISTENT_COUNT = 5 #No. of DPD update periods for which the error needs to persist to trigger a persistent error  
    
    dpdFaultConditionArr = Array.CreateInstance(Types.adi_adrv9010_DpdFaultCondition_t, 1)
    dpdFaultConditionArr[0] = Types.adi_adrv9010_DpdFaultCondition_t()
    dpdFaultConditionArr[0].dpdMetric = Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_INDIRECT_EVM
    dpdFaultConditionArr[0].comparator = Types.adi_adrv9010_DpdComparator_e.ADI_ADRV9010_DPD_COMPARATOR_GREATER_THAN
    dpdFaultConditionArr[0].threshold0 = INDIRECT_EVM_THRESH0_PERCENTAGE
    dpdFaultConditionArr[0].threshold1 = INDIRECT_EVM_THRESH1_PERCENTAGE
    dpdFaultConditionArr[0].persistentCount = ERROR_PERSISTENT_COUNT
    #Program the indirect fault condition definition
    link.platform.board.Adrv9010Device.Dfe.DpdFaultConditionSet(txChannelMask, dpdFaultConditionArr, 1)

    #Setup Recovery Action
    dpdRecoveryActionArr = Array.CreateInstance(Types.adi_adrv9010_DpdRecoveryActionConfig_t, 4)   
    
    thresh0ActionMaskPersistent = 0
    #thresh0ActionMaskPersistent |= int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_SKIP_LUTS_UPDATE)
    thresh0ActionMaskPersistent |= int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_REVERT_LUTS_TO_UNITY)
    #thresh0ActionMaskPersistent |= int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_RESET_ADAPTATION_STATE)
    
    #Recovery Action for violation of threshold1 - skip LUT updates, restore LUT to unity and reset adaptation state for violation of hard threshold
    thresh1ActionMaskPersistent = 0
    #thresh1ActionMaskPersistent |= int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_SKIP_LUTS_UPDATE)
    #thresh1ActionMaskPersistent |= int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_REVERT_LUTS_TO_UNITY)
    #thresh1ActionMaskPersistent |= int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_RESET_ADAPTATION_STATE)

    #Configure Recovery Action for violation of threshold0
    dpdRecoveryActionArr[0] = Types.adi_adrv9010_DpdRecoveryActionConfig_t()
    dpdRecoveryActionArr[0].dpdErrorState = Types.adi_adrv9010_DpdErrorState_e.ADI_ADRV9010_DPD_ERR_STATE_0
    dpdRecoveryActionArr[0].dpdRecoveryAction.dpdMetricsMask = int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_INDIRECT_ERROR)
    #dpdRecoveryActionArr[0].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_TU_POWER)
    #dpdRecoveryActionArr[0].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_ORX_POWER)
    dpdRecoveryActionArr[0].dpdRecoveryAction.dpdActionMask = int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_SKIP_LUTS_UPDATE)

    #Configure Recovery Action for violation of threshold1
    dpdRecoveryActionArr[1] = Types.adi_adrv9010_DpdRecoveryActionConfig_t()
    dpdRecoveryActionArr[1].dpdErrorState = Types.adi_adrv9010_DpdErrorState_e.ADI_ADRV9010_DPD_ERR_STATE_1
    dpdRecoveryActionArr[1].dpdRecoveryAction.dpdMetricsMask = int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_DIRECT_EVM)
    dpdRecoveryActionArr[1].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_TU_POWER)
    #dpdRecoveryActionArr[1].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_ORX_POWER)
    dpdRecoveryActionArr[1].dpdRecoveryAction.dpdActionMask = int(Types.adi_adrv9010_DpdRecoveryAction_e.ADI_ADRV9010_DPD_RECOVERY_ACTION_SKIP_LUTS_UPDATE)

    #Configure Recovery Action for persistent violation of threshold0
    dpdRecoveryActionArr[2] = Types.adi_adrv9010_DpdRecoveryActionConfig_t()
    dpdRecoveryActionArr[2].dpdErrorState = Types.adi_adrv9010_DpdErrorState_e.ADI_ADRV9010_DPD_ERR_STATE_PERSISTENT_0
    dpdRecoveryActionArr[2].dpdRecoveryAction.dpdMetricsMask = int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_DIRECT_EVM)
    dpdRecoveryActionArr[2].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_TU_POWER)
    #dpdRecoveryActionArr[2].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_ORX_POWER)
    dpdRecoveryActionArr[2].dpdRecoveryAction.dpdActionMask = thresh0ActionMaskPersistent

    #Configure Recovery Action for persistent violation of threshold1
    dpdRecoveryActionArr[3] = Types.adi_adrv9010_DpdRecoveryActionConfig_t()
    dpdRecoveryActionArr[3].dpdErrorState = Types.adi_adrv9010_DpdErrorState_e.ADI_ADRV9010_DPD_ERR_STATE_PERSISTENT_1
    #dpdRecoveryActionArr[3].dpdRecoveryAction.dpdMetricsMask = int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_DIRECT_EVM)
    dpdRecoveryActionArr[3].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_TU_POWER)
    #dpdRecoveryActionArr[3].dpdRecoveryAction.dpdMetricsMask |= int(Types.adi_adrv9010_DpdMetric_e.ADI_ADRV9010_DPD_METRIC_MEAN_ORX_POWER)
    dpdRecoveryActionArr[3].dpdRecoveryAction.dpdActionMask = thresh1ActionMaskPersistent

    #Program the recovery action in the device
    link.platform.board.Adrv9010Device.Dfe.DpdRecoveryActionSet(txChannelMask, dpdRecoveryActionArr, 4)
    print"***************************************"

def dpdTrackingConfigSet( txChMask = 0xF):
    print"***************************************"
    print"Setting up DPD Tracking Config"
    dpdTrackCfg = Types.adi_adrv9010_DpdTrackingConfig_t()
    dpdTrackCfgGet = Types.adi_adrv9010_DpdTrackingConfig_t()
    retVal = link.platform.board.Adrv9010Device.Dfe.DpdTrackingConfigGet(Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX1,dpdTrackCfgGet)
    dpdTrackCfg = retVal[1]
    MThreshold_dBFS = -21
    FULL_SCALE_CODE = 32768
    temp = pow(10,(MThreshold_dBFS/20.0))*FULL_SCALE_CODE
    dpdTrackCfg.dpdMThreshold = pow(temp,2)
    dpdTrackCfg.dpdPeakSearchWindowSize = 16384 * 50
    dpdTrackCfg.dpdRegularizationValue = 20
    dpdTrackCfg.dpdSamples = 16384*2
    dpdTrackCfg.dpdUpdateMode =  Types.adi_adrv9010_DpdTrackingUpdateMode_e.ADI_ADRV9010_DPD_TRACKING_UPDATE_MODE_1 #intDpdDynamicMode.ADI_ADRV9010_DPD_TRACKING_UPDATE_MODE_1
    dpdTrackCfg.txChannelMask = txChMask
    link.platform.board.Adrv9010Device.Dfe.DpdTrackingConfigSet(dpdTrackCfg)
    print"DPD M Threshold = ",dpdTrackCfg.dpdMThreshold
    print"DPD Peak Search Window Size = ",dpdTrackCfg.dpdPeakSearchWindowSize
    print"DPD Regularization Value = ",dpdTrackCfg.dpdRegularizationValue
    print"DPD Update Mode = ",dpdTrackCfg.dpdUpdateMode
    print"***************************************"
	
def dpdEnableTracking(txChMask = 0xF, enable = 0):
    calMaskList = [Types.adi_adrv9010_TrackingCalibrations_e.ADI_ADRV9010_TRACK_TX1_DPD, Types.adi_adrv9010_TrackingCalibrations_e.ADI_ADRV9010_TRACK_TX2_DPD, 
                   Types.adi_adrv9010_TrackingCalibrations_e.ADI_ADRV9010_TRACK_TX3_DPD, Types.adi_adrv9010_TrackingCalibrations_e.ADI_ADRV9010_TRACK_TX4_DPD]
    txChList = [1, 2, 3, 4]
    calMask = 0
    for ii in range(len(txChList)):
        if(txChMask & 0x1<<ii):
            calMask |= int(calMaskList[ii])
            print (calMaskList[ii])
            print (txChMask & 0x1<<ii)
            print hex(calMask)
    if enable:
        link.platform.board.Adrv9010Device.Cals.TrackingCalsEnableSet(calMask, Types.adi_adrv9010_TrackingCalEnableDisable_e.ADI_ADRV9010_TRACKING_CAL_ENABLE)
    else:
        link.platform.board.Adrv9010Device.Cals.TrackingCalsEnableSet(calMask, Types.adi_adrv9010_TrackingCalEnableDisable_e.ADI_ADRV9010_TRACKING_CAL_DISABLE)
    print "Enabled tracking cals:", hex(link.platform.board.Adrv9010Device.Cals.TrackingCalsEnableGet(calMask)[1]) 

def dpdStatusGet(txChannel):
    dpdStatus = Types.adi_adrv9010_DpdStatus_t()
    retVal = link.platform.board.Adrv9010Device.Dfe.DpdStatusGet(txChannel, dpdStatus)
    dpdStatus = retVal[1]
    meanTu = dpdStatus.dpdStatistics.dpdMeanTuPower
    peakTu = dpdStatus.dpdStatistics.dpdPeakTuPower
    meanTx = dpdStatus.dpdStatistics.dpdMeanTxPower + 0.00001  #avoid the math domain error
    peakTx = dpdStatus.dpdStatistics.dpdPeakTxPower + 0.00001  #avoid the math domain error
    meanOrx = dpdStatus.dpdStatistics.dpdMeanOrxPower + 0.00001
    peakOrx = dpdStatus.dpdStatistics.dpdPeakOrxPower + 0.00001
    print "dpdErrorCode:",dpdStatus.dpdErrorCode
    print "dpdPercentComplete",dpdStatus.dpdPercentComplete
    print "dpdPerformanceMetric",dpdStatus.dpdPerformanceMetric
    print "dpdIterCount",dpdStatus.dpdIterCount
    print "dpdUpdateCount",dpdStatus.dpdUpdateCount
    print "dpdDirectEvm",dpdStatus.dpdStatistics.dpdDirectEvm
    print "dpdIndirectError",dpdStatus.dpdStatistics.dpdIndirectError
    print "dpdIndirectEvm",dpdStatus.dpdStatistics.dpdIndirectEvm
    print "dpdSelectError",dpdStatus.dpdStatistics.dpdSelectError
    if int(meanTu*10 + peakTu*10 + meanTx*10 + peakTx*10 + meanOrx*10 + peakOrx*10) != 0: 
        print "dpdMeanTuPower",20*log10(sqrt(meanTu) / 32768) 
        print "dpdPeakTuPower",20*log10(sqrt(peakTu) / 32768) 
        print "dpdMeanTxPower",20*log10(sqrt(meanTx) / 32768) 
        print "dpdPeakTxPower",20*log10(sqrt(peakTx) / 32768) 
        print "dpdMeanOrxPower",20*log10(sqrt(meanOrx) / 32768) 
        print "dpdPeakOrxPower",20*log10(sqrt(peakOrx) / 32768) 
    print "dpdErrorStatus0 (metrics:actions): X:X", dpdStatus.dpdErrorStatus0.dpdMetricsMask, dpdStatus.dpdErrorStatus0.dpdActionMask 
    print "dpdErrorStatus1 (metrics:actions): X:X", dpdStatus.dpdErrorStatus1.dpdMetricsMask, dpdStatus.dpdErrorStatus1.dpdActionMask 
    print "dpdPersistentErrorStatus0 (metrics:actions): X:X", dpdStatus.dpdPersistentErrorStatus0.dpdMetricsMask, dpdStatus.dpdPersistentErrorStatus0.dpdActionMask 
    print "dpdPersistentErrorStatus1 (metrics:actions): X:X", dpdStatus.dpdPersistentErrorStatus1.dpdMetricsMask, dpdStatus.dpdPersistentErrorStatus1.dpdActionMask 

def runExtPathDelayInitCal(chMask):
    initCal = Types.adi_adrv9010_InitCals_t()
    initCal.calMask = int(Types.adi_adrv9010_InitCalibrations_e.ADI_ADRV9010_EXTERNAL_PATH_DELAY)
    initCal.channelMask = chMask
    initCal.warmBoot = 0

    print "calMask:", hex(initCal.calMask)
    link.platform.board.Adrv9010Device.Cals.InitCalsRun(initCal)
    print "Path delay cal blocking wait status:", link.platform.board.Adrv9010Device.Cals.InitCalsWait(3000, 0)[1]

def getExtPathDelay(txCh):

    extPathDelay = Types.adi_adrv9010_ExternalPathDelay_t()
    retVal = link.platform.board.Adrv9010Device.Cals.ExternalPathDelayGet(txCh, extPathDelay)
    extPathDelay = retVal[1]
    print "fifoDelay:",extPathDelay.fifoDelay
    print "interpolationIndex:", extPathDelay.interpolationIndex

def setExtPathDelay(txCh, fifoDel, interpIndex):
    externalPathDelay = Types.adi_adrv9010_ExternalPathDelay_t()
    externalPathDelay.fifoDelay = fifoDel
    externalPathDelay.interpolationIndex = interpIndex
    link.platform.board.Adrv9010Device.Cals.ExternalPathDelaySet(txCh,externalPathDelay)
#Create an Instance of the Class
link = AdiEvaluationSystem.Instance	
connect = False

if (link.IsConnected() == False):
    connect = True
    link.platform.board.Client.Connect("192.168.1.10", 55556) 
    print "Connecting"

if (link.IsConnected()):
    adrv9010 = link.Adrv9010Get(1)
    print "Connected"
    # If already under TDD radio control mode, Quit pin contorl mode
    RadioControl = Types.adi_adrv9010_RadioCtrlModeCfg_t()
    RadioControl.txRadioCtrlModeCfg.txChannelMask = 0xF
    RadioControl.txRadioCtrlModeCfg.txEnableMode = Types.adi_adrv9010_TxEnableMode_e.ADI_ADRV9010_TX_EN_SPI_MODE
    RadioControl.rxRadioCtrlModeCfg.rxChannelMask = 0xF
    RadioControl.rxRadioCtrlModeCfg.rxEnableMode = Types.adi_adrv9010_RxEnableMode_e.ADI_ADRV9010_RX_EN_SPI_MODE
    RadioControl.orxRadioCtrlModeCfg.orxEnableMode = Types.adi_adrv9010_ORxEnableMode_e.ADI_ADRV9010_ORX_EN_SPI_MODE
    # Disable TX/RX/ORX path
    link.platform.board.Adrv9010Device.RadioCtrl.RxTxEnableSet(0,0)
    ##### YOUR CODE GOES HERE #####
    status = adrv9010.RadioCtrl.RxTxEnableGet(0,0)
    print "Rx status: ", hex(status[1]), ", Tx Status: ",hex(status[2])
##########################
### DPD 的同用具体使用 ###
##########################
    # for tx1 set to 1, tx2 = 2, tx3 = 4 and tx4 = 8) #dpd modle 和 dpd reset 通用设置
    runExtPathDelayInitCal(0x1)         # Run 1st after loading signal-> PA on -> Settign Tx atten and ORx gain index
    time.sleep(1) #睡眠1秒
    dpdModelConfigSet()                 # Run 2rd - load the model from file （可以查看dpdmodel的config的设置）
    dpdIndirectEvmStabilityConfigSet()  # Run 3rd Setup Indirect EVM stability config(fault condition + recovery action)
    resetDpdFull(1)                     # Run 4th Full reset the DPD（dpd的reset的设置）
    time.sleep(1)                       # 然后在睡眠1秒
    dpdEnableTracking(0x1,1)            # Run 5th to enable DPD tracking（dpd的使能配置）
    # Enable TX1 path
    link.platform.board.Adrv9010Device.RadioCtrl.RxTxEnableSet(0,1)
    time.sleep(10) #在最后的dpd配置睡眠10秒
    dpdStatusGet(Types.adi_adrv9010_TxChannels_e.ADI_ADRV9010_TX1) # Run 6th to get the DPD status #最后一步查看所有的dpd的配置
    #DPD GET STATUS 可以查看到所有的DPD的使能状态

    
else:
    print "Not Connected"

if (connect):
    link.platform.board.Client.Disconnect()
    print "Disconnected"
