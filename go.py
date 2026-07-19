# -*- coding: utf-8 -*-
import sys
import os
import importlib.util

def load_so_module():
    # လက်ရှိ folder ထဲရှိ two.so (သို့မဟုတ် 2.so) ဖိုင်လမ်းကြောင်းကို သတ်မှတ်ခြင်း
    # (သင့် script အရ လက်ရှိဖိုင်က two.so အဖြစ် ပြောင်းလဲထားပုံရသည်)
    so_path = os.path.join(os.path.dirname(__file__), "two.so")
    
    # အကယ်၍ two.so မရှိရင် cpython အရှည်နဲ့ဖိုင်ကို ရှာကြည့်ခြင်း
    if not os.path.exists(so_path):
        for file in os.listdir(os.path.dirname(__file__)):
            if file.startswith("two.cpython") and file.endswith(".so"):
                so_path = os.path.join(os.path.dirname(__file__), file)
                break

    if not os.path.exists(so_path):
        print("\033[1;31m[-] two.so ဖိုင်ကို ရှာမတွေ့ပါ။ စနစ်ကို မောင်းနှင်၍မရပါ။\033[0m")
        sys.exit(1)

    try:
        # ⚠️ အရေးကြီးဆုံးနေရာ - မူရင်း Cython ဖိုင်နာမည် 'two' နှင့် ကိုက်ညီအောင် ပြင်ဆင်ခြင်း
        spec = importlib.util.spec_from_file_location("two", so_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"\033[1;31m[-] ဖိုင်ဖတ်ရာတွင် အမှားအယွင်းရှိနေသည်: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main_logic = load_so_module()
    
    try:
        # .so ထဲမှ ပင်မ Function ကို လှမ်းခေါ်ခြင်း
        main_logic.run_system()
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] အစီအစဉ်ကို အသုံးပြုသူမှ ရပ်တန့်လိုက်သည်။\033[0m")
        sys.exit(0)
