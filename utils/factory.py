def get_model(model_name, args):
    name = model_name.lower()
    if name == "icarl":
        from models.icarl import iCaRL
        return iCaRL(args)
    if name == "icarl_random":
        from models.icarl_random import iCaRL_Random
        return iCaRL_Random(args)
    elif name == "icarl_dm":
        from models.icarl_dm import iCaRL_DM
        return iCaRL_DM(args)
    elif name == "icarl_sre2l":
        from models.icarl_sre2l import iCaRL_Sre2L
        return iCaRL_Sre2L(args)
    elif name == "icarl_cafe":
        from models.icarl_cafe import iCaRL_CAFE
        return iCaRL_CAFE(args)
    elif name == "icarl_dam":
        from models.icarl_dam import iCaRL_DataDAM
        return iCaRL_DataDAM(args)
    elif name == "bic":
        from models.bic import BiC
        return BiC(args)
    elif name == "podnet":
        from models.podnet import PODNet
        return PODNet(args)
    elif name == "lwf":
        from models.lwf import LwF
        return LwF(args)
    elif name == "ewc":
        from models.ewc import EWC
        return EWC(args)
    elif name == "wa":
        from models.wa import WA
        return WA(args)
    elif name == "der":
        from models.der import DER
        return DER(args)
    elif name == "finetune":
        from models.finetune import Finetune
        return Finetune(args)
    elif name == "replay":
        from models.replay import Replay
        return Replay(args)
    elif name == "gem":
        from models.gem import GEM
        return GEM(args)
    elif name == "coil":
        from models.coil import COIL
        return COIL(args)
    elif name == "foster":
        from models.foster import FOSTER
        return FOSTER(args)
    elif name == "foster_dm":
        from models.foster_dm import FOSTER_DM
        return FOSTER_DM(args)
    elif name == "foster_sre2l":
        from models.foster_sre2l import FOSTER_SRE2L
        return FOSTER_SRE2L(args)
    elif name == "rmm-icarl":
        from models.rmm import RMM_FOSTER, RMM_iCaRL
        return RMM_iCaRL(args)
    elif name == "rmm-foster":
        from models.rmm import RMM_FOSTER, RMM_iCaRL
        return RMM_FOSTER(args)
    elif name == "fetril":
        from models.fetril import FeTrIL 
        return FeTrIL(args)
    elif name == "pass":
        from models.pa2s import PASS
        return PASS(args)
    elif name == "il2a":
        from models.il2a import IL2A
        return IL2A(args)
    elif name == "ssre":
        from models.ssre import SSRE
        return SSRE(args)
    elif name == "memo":   
        from models.memo import MEMO
        return MEMO(args)
    elif name == "beefiso":
        from models.beef_iso import BEEFISO
        return BEEFISO(args)
    elif name == "beefiso_dm":
        from models.beef_iso_dm import BEEFISO_DM
        return BEEFISO_DM(args)
    elif name == "simplecil":
        from models.simplecil import SimpleCIL
        return SimpleCIL(args)
    else:
        assert 0
