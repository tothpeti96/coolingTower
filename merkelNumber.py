import math

class RK4:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.param = []

    def getNewValue(self):
        v0 = self.value
        p1 = self.param[0]
        p2 = self.param[1]
        p3 = self.param[2]
        p4 = self.param[3]
        return v0 + (p1 + 2 * p2 + 2 * p3 + p4)/6

"""
INPUT DATA FOR COOLING TOWER (GLOBAL VARIABLES)

"""

T_wi = 39.67 + 273.15    #312.75
T_wo = 27.77 + 273.15   #300.92
w = 0.00616336          #kg/kg
i_ma = 25291.87496      #J/kg
p_abs = 101712.27       # Pa
n = 2                   # db
m_wi = 3.999            # kg/s
m_a = 4.134             # kg/s

"""
PROPERTY FUNCTIONS
"""
def get_c_pa(T):
    # Specific heat capacity of dry air
     return 1.045356 * 10**3 - 3.161783 * 10 ** (-1) * T + 7.083814 * 10 ** (-4) * T ** 2 - 2.705209 * 10 ** (-7) * T ** 3 

def get_c_pv(T):
    # Specific heat capacity of vapour
    return 1.3605 * 10 ** 3 + 2.31334 * T - 2.46784 * 10 ** (-10) * T ** 5 + 5.91332 * 10 ** (-13) * T ** 6

def get_c_pw(T):
    # Specific heat capacity of water
    return 8.15599 * 10 ** 3 - 2.80627 * 10 * T + 5.11283 * 10 ** (-2) * T ** 2 - 2.17582 * 10 ** (-13) * T ** 6

def get_p_wv(T):
    # Pressure 
    return 10 ** (10.79586 * (1-(273.15/T)) + 5.02808 * math.log(273.15/T, 10) + 1.50474 * 10 ** (-4) * (1 - 10 ** (-8.29692 * (T/273.15)-1)) + 4.2873 * 10 ** (-4) * ((10 ** (4.76955 * (1- 273.16/T)))-1) + 2.786)

def get_w_ws(p_abs, p_vwb):
    # Humidity ratio for saturated air
    return (0.62509 * p_vwb)/(p_abs - 1.005 * p_vwb)

def get_i_fgw(T):
    # Latent heat of water at 0°C
    return 3.4831814 * 10 ** 6 - 5.8627703 * 10 ** 3 * T + 12.139568 * T ** 2 - 1.40290431 * 10 ** (-2) * T ** 3 

def get_i_v(i_fgw, c_pv, T_w):
    # Enthalpy of water vapor at local bulk water temperature
    return i_fgw + c_pv * (T_w - 273.15)

def get_i_masw(c_pa, T, w, i_v):
    # Enthalpy of saturated air at local bulk water temperature
    return c_pa * (T-273.15) + w * i_v

def get_Le(w_sw, w):
    # Lewis factor of the given intersect
    return 0.865 ** 0.667 * (((w_sw + 0.622)/(w + 0.622) - 1))/(math.log(((w_sw + 0.622) / (w + 0.622)), math.e))

def get_mv_ma(m_wi, m_a, w_i):
    # Mass balance at given intersection
    return  m_wi / m_a * (1 - m_a/m_wi * (0.02226 - w_i))

def get_j(delta_Tw, c_pw, mw_ma, w_ws, w0, i_masw, i_ma_n, Le, i_v, T_w):
    return delta_Tw * ((c_pw * mw_ma * (w_ws - w0))/(i_masw - i_ma_n + (Le - 1) * (i_masw - i_ma_n - (w_ws - w0)*i_v) - (w_ws - w0) * c_pw * (T_w - 273.15)))
    
def get_k(delta_Tw, c_pw, mw_ma, w_sw, w0, T_w, i_masw, i_ma_0, Le, i_v):
    return delta_Tw * c_pw * mw_ma * (1 + ((w_sw - w0) * c_pw * T_w)/(i_masw - i_ma_0 + (Le - 1) * (i_masw - i_ma_0 - (w_sw - w) * i_v) - (w_sw - w0) * c_pw * T_w))

def get_l(delta_Tw, c_pw, i_masw, Le, w_sw, i_v, w_0, Tw, i_ma_n):
    return (delta_Tw * c_pw)/(i_masw - i_ma_n + (Le - 1) * (i_masw - i_ma_n - (w_sw - w) * i_v) - (w_sw - w_0) * c_pw * Tw)

def getDB(Enth, X):
    return (Enth/1000 - 2501 * X) / (1.006 + 1.86 * X) + 273.15

def getWB(X):
    return (math.log(X/ 0.0039)) / 0.0656 + 273.15

def get_i_ma(c_pv_act, c_pa_act, T_db_act, X_act):
    return c_pa_act * (T_db_act - 273.15) + X_act * (2501598 + c_pv_act * (T_db_act - 273.15))

def get_w(T_wb, T, p_vwb, p_abs):
    return ((2501.6 - 2.3263 * (T_wb - 273.15)) / (2501.6 + 1.8577 * (T - 273.15) - 4.184 * (T_wb - 273.15))) * ((0.62509 * p_vwb)/(p_abs - 1.005 * p_vwb)) - ((1.00416 * (T - T_wb))/(2501.6 + 1.8577 * (T - 273.15) - 4.184 * (T_wb - 273.15)))
    
def get_satT(p_v):
    return 164.630366 + 1.832295 * 10 ** (-3) * p_v + 4.27215 * 10 ** (-10) * p_v ** 2 + 3.738954 * 10 ** 3 * p_v ** (-1) - 7.01204 * 10 ** 5 * p_v ** (-2) + 16.161488 * math.log(p_v) - 1.437169 * 10 ** (-4) * p_v * math.log(p_v)
"""
CHECK SATURATION LEVEL
"""

def checkSaturation(i_ma_act, x_act):

    T_db = getDB(i_ma_act, x_act)
    T_wb = getWB(x_act)

    if T_wb > T_db:
        return True
    else:
        return False

"""
MAIN CYCLE
"""

def main():

    T_wi = 39.67 + 273.15    #312.75
    T_wo = 27.77 + 273.15   #300.92
    w = 0.00616336          #kg/kg
    i_ma = 25291.87496      #J/kg
    p_abs = 101712.27       # Pa
    n = 2                   # db
    m_wi = 3.999            # kg/s
    m_a = 4.134             # kg/s

    Humidity = []
    Enthalpy = []
    Merkel = []
    Temperature = []

    Humidity.append(w)
    Enthalpy.append(i_ma)
    Merkel.append(0)
    Temperature.append(T_wo)

    SAT = False

    step = 2
    delta_T_w = round((T_wi - T_wo)/n, 4)
    for i in range(step):
                
        w_n = Humidity[-1]
        i_ma_n = Enthalpy[-1]
        Me_n = Merkel[-1]
        T_w_n  = Temperature[-1]

        # Humidity ratio of air
        J = RK4("j", w_n)
        # Enthalpy of air
        K = RK4("k", i_ma_n)
        # Merkel constant of the cooling tower
        L = RK4("k", Me_n)

        T_w_0 = T_w_n
        for i in range(4):

            if SAT == False:
                T_mid = (T_w_n + 273.15)/2
                c_pa = get_c_pa(T_mid)
                c_pv = get_c_pv(T_mid)
                c_pw = get_c_pw(T_mid)
                p_wv = get_p_wv(T_w_n)
                w_ws = get_w_ws(p_abs, p_wv)
                i_fgw = get_i_fgw(273.15)
                i_v = get_i_v(i_fgw, c_pv, T_w_n)
                i_masw = get_i_masw(c_pa, T_w_n , w_ws, i_v)
                Le = get_Le(w_ws, w_n)
                mw_ma = get_mv_ma(m_wi, m_a, w_n)
                j = get_j(delta_T_w, c_pw, mw_ma, w_ws, w_n, i_masw, i_ma_n, Le, i_v, T_w_n)
                # j = round(j,6)
                J.param.append(j)
                k = get_k(delta_T_w, c_pw, mw_ma, w_ws, w_n, T_w_n-273.15, i_masw, i_ma_n, Le, i_v)
                # k = round(k,2)
                K.param.append(k)
                l = get_l(delta_T_w, c_pw, i_masw, Le, w_ws, i_v, w_n, T_w_n-273.15, i_ma_n)
                # l = round(l,5)
                L.param.append(l)
            else:
                T_wb = getWB(Humidity[-1])
                T_db = getDB(Enthalpy[-1], Humidity[-1])
                T_wb= (T_wb + T_db)/2
                p_vwb = get_p_wv(T_wb)
                # w_sa = get_w(T_wb, get_satT(p_vwb), p_vwb, p_abs)
                w_sa = get_w(T_wb, get_satT(p_vwb), p_vwb, p_abs)
                T_mid = (T_w_n + 273.15)/2
                c_pa = get_c_pa(T_mid)
                c_pv = get_c_pv(T_mid)
                c_pw = get_c_pw(T_mid)
                p_wv = get_p_wv(T_w_n)
                w_ws = get_w_ws(p_abs, p_wv)
                i_fgw = get_i_fgw(273.15)
                i_v = get_i_v(i_fgw, c_pv, T_w_n)
                i_masw = get_i_masw(c_pa, T_w_n , w_ws, i_v)
                Le = get_Le(w_ws, w_n)
                mw_ma = get_mv_ma(m_wi, m_a, w_n)
                j = get_j(delta_T_w, c_pw, mw_ma, w_ws, w_sa, i_masw, i_ma_n, Le, i_v, T_w_n)
                # j = round(j,6)
                J.param.append(j)
                k = get_k(delta_T_w, c_pw, mw_ma, w_ws, w_sa, T_w_n-273.15, i_masw, i_ma_n, Le, i_v)
                # k = round(k,2)
                K.param.append(k)
                l = get_l(delta_T_w, c_pw, i_masw, Le, w_ws, i_v, w_sa, T_w_n-273.15, i_ma_n)
                # l = round(l,5)
                L.param.append(l)

            if i == 2:
                i_ma_n = K.value + k 
                w_n = J.value + j    
                T_w_n = T_w_0 + delta_T_w
            else:
                i_ma_n = K.value + k/2 
                w_n = J.value + j/2 
                T_w_n = T_w_0 + delta_T_w/2
            print()
        
        Humidity.append((J.getNewValue()))
        Enthalpy.append((K.getNewValue()))
        Merkel.append((L.getNewValue()))
        Temperature.append(Temperature[-1] + delta_T_w)

        print()

        if SAT == False:
            if checkSaturation(Enthalpy[-1], Humidity[-1]):
                SAT = True

main()