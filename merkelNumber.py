# import math

# class RK4:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
#         self.param = []

#     def getNewValue(self):
#         v0 = self.value
#         p1 = self.param[0]
#         p2 = self.param[1]
#         p3 = self.param[2]
#         p4 = self.param[3]
#         return v0 + (p1 + 2 * p2 + 2 * p3 + p4)/6

# """
# EQUATIONS GOVERNING THE MERKEL NUMBER CALCULATION METHOD
# """

# def get_j(delta_Tw, c_pw, mw_ma, w_ws, w0, i_masw, i_ma_n, Le, i_v, T_w):
#     return delta_Tw * ((c_pw * mw_ma * (w_ws - w0))/(i_masw - i_ma_n + (Le - 1) * (i_masw - i_ma_n - (w_ws - w0)*i_v) - (w_ws - w0) * c_pw * (T_w - 273.15)))
    
# def get_k(delta_Tw, c_pw, mw_ma, w_sw, w0, T_w, i_masw, i_ma_0, Le, i_v):
#     return delta_Tw * c_pw * mw_ma * (1 + ((w_sw - w0) * c_pw * T_w)/(i_masw - i_ma_0 + (Le - 1) * (i_masw - i_ma_0 - (w_sw - w0) * i_v) - (w_sw - w0) * c_pw * T_w))

# def get_l(delta_Tw, c_pw, i_masw, Le, w_sw, i_v, w_0, Tw, i_ma_n):
#     return (delta_Tw * c_pw)/(i_masw - i_ma_n + (Le - 1) * (i_masw - i_ma_n - (w_sw - w_0) * i_v) - (w_sw - w_0) * c_pw * Tw)

# """
# EQUATIONS GOVERNING THE COOLING TOWER THERMODYNAMICS
# """
# # Unsaturated case

# def get_dX_dz(baaz, w_s, w, m_a):
#     return (baaz * w_s - w) / m_a

# def get_dmw_dz(baaz, X_s_w, X_s_a):
#     return baaz * (X_s_w - X_s_a)

# def get_dTa_dz(baaz, Le, T_w, T_a, c_pa, c_pv, w, w_s, m_a):
#     return baaz * (Le * (T_w - T_a) * (c_pa + c_pv * w) + (c_pv * T_w - c_pv * T_a) * (w_s - w)) /(m_a * (c_pa + c_pv * w))

# def get_dTw_dz(baaz, Le, T_w, T_a, c_pa, c_pv, r_0, c_w, X_s, X, m_w):
#     return baaz * (Le * (T_w - T_a) * (c_pa + c_pv * X) + (r_0 + c_pv * T_w - c_w * T_w) * (X_s - X)) / (m_w * c_w)

# def get_dha_dz(c_pa_a, w, c_pv_a, dTa_dZ, T_a, dX_dZ):
#     return (c_pa_a + w * c_pv_a) * dTa_dZ + (2501598 + c_pv_a * T_a) * dX_dZ

# # Saturated case

# def get_dmw_dz_sat(baaz, X_s_w, X_s_a):
#     return baaz * (X_s_w - X_s_a)

# def get_dX_dZ_sat(baaz, X_s_w, X_s_a, m_a):
#     return (baaz * (X_s_w - X_s_a)) / m_a

# def get_dTa_dZ_sat(baaz, m_a, c_pa, Le, T_a, T_w, X_s_w, r_0, c_pv_w, c_w_a, X, X_s_a, c_pv_a, c_pa_a, dX_dT):
#     return - 1 * ((baaz / m_a) * (c_pa * Le * (T_a - T_w) - X_s_w * (r_0 + c_pv_w * T_w) + c_w_a * (Le * (T_a - T_w) * (X - X_s_a) + T_a * (X_s_w - X_s_a)) + X_s_a * (r_0 + c_pv_a * Le * (T_a - T_w) + c_pv_w * T_w)) / (c_pa_a + c_w_a * X + dX_dT * (r_0 + c_pv_a * T_a - c_w_a * T_a) + X_s_a * (c_pv_a - c_w_a)))

# def get_dTw_dZ_sat(baaz, r_0, c_pv_w, T_w, c_w_w, X_s_w, X_s_a, Le, T_a, c_pa_a, c_w_a, X, c_pv_a, m_w):
#     return baaz * ((r_0 + c_pv_w * T_w - c_w_w * T_w) * (X_s_w - X_s_a) + Le * (T_w - T_a) * (c_pa_a + c_w_a * (X - X_s_a) + c_pv_a * X_s_a)) / (c_w_w * m_w)

# def get_dha_dz_sat(c_pv_a, T_a, c_w_a, dX_dTa, w_s_a, c_p_v, c_pa_a, w, dX_dZ):
#     return ((2501598 + c_pv_a * T_a - c_w_a * T_a) * dX_dTa + w_s_a * (c_p_v - c_w_a) + c_pa_a + w * c_w_a) + c_w_a * T_a * dX_dZ

# """
# PROPERTY FUNCTIONS
# """

# def get_Beta_a_Az(Me, m_w, H):
#     # Heat condoctivity and diffusitivity constant of given cooling tower derived from previously determined Merkel number.
#     baaz = Me * m_w / H
#     return baaz

# def get_c_pa(T):
#     # Specific heat capacity of dry air
#      return 1.045356 * 10**3 - 3.161783 * 10 ** (-1) * T + 7.083814 * 10 ** (-4) * T ** 2 - 2.705209 * 10 ** (-7) * T ** 3 

# def get_c_pv(T):
#     # Specific heat capacity of vapour
#     return 1.3605 * 10 ** 3 + 2.31334 * T - 2.46784 * 10 ** (-10) * T ** 5 + 5.91332 * 10 ** (-13) * T ** 6

# def get_c_pw(T):
#     # Specific heat capacity of water
#     return 8.15599 * 10 ** 3 - 2.80627 * 10 * T + 5.11283 * 10 ** (-2) * T ** 2 - 2.17582 * 10 ** (-13) * T ** 6

# def get_p_wv(T):
#     # Pressure 
#     return 10 ** (10.79586 * (1-(273.15/T)) + 5.02808 * math.log(273.15/T, 10) + 1.50474 * 10 ** (-4) * (1 - 10 ** (-8.29692 * (T/273.15)-1)) + 4.2873 * 10 ** (-4) * ((10 ** (4.76955 * (1- 273.16/T)))-1) + 2.786)

# def get_w_ws(p_abs, p_vwb):
#     # Humidity ratio for saturated air
#     return (0.62509 * p_vwb)/(p_abs - 1.005 * p_vwb)

# def get_i_fgw(T):
#     # Latent heat of water at 0°C
#     return 3.4831814 * 10 ** 6 - 5.8627703 * 10 ** 3 * T + 12.139568 * T ** 2 - 1.40290431 * 10 ** (-2) * T ** 3 

# def get_i_v(i_fgw, c_pv, T_w):
#     # Enthalpy of water vapor at local bulk water temperature
#     return i_fgw + c_pv * (T_w - 273.15)

# def get_i_masw(c_pa, T, w, i_v):
#     # Enthalpy of saturated air at local bulk water temperature
#     return c_pa * (T-273.15) + w * i_v

# def get_Le(w_sw, w):
#     # Lewis factor of the given intersect
#     return 0.865 ** 0.667 * (((w_sw + 0.622)/(w + 0.622) - 1))/(math.log(((w_sw + 0.622) / (w + 0.622)), math.e))

# def get_mv_ma(m_wi, m_a, w_i):
#     # Mass balance at given intersection
#     return  m_wi / m_a * (1 - m_a/m_wi * (0.02226 - w_i))

# def getDB(Enth, X):
#     #Dry bulb temperature of air
#     return (Enth/1000 - 2501 * X) / (1.006 + 1.86 * X) + 273.15

# def getWB(X):
#     # Wet bulb temperature of air
#     return (math.log(X/ 0.0039)) / 0.0656 + 273.15

# def get_i_ma(c_pv_act, c_pa_act, T_db_act, X_act):
#     # Specific enthalpy of humid air
#     return c_pa_act * (T_db_act - 273.15) + X_act * (2501598 + c_pv_act * (T_db_act - 273.15))

# def get_w(T_wb, T, p_vwb, p_abs):
#     # Humidity of air in kg water / kg air
#     return ((2501.6 - 2.3263 * (T_wb - 273.15)) / (2501.6 + 1.8577 * (T - 273.15) - 4.184 * (T_wb - 273.15))) * ((0.62509 * p_vwb)/(p_abs - 1.005 * p_vwb)) - ((1.00416 * (T - T_wb))/(2501.6 + 1.8577 * (T - 273.15) - 4.184 * (T_wb - 273.15)))
    
# def get_satT(p_v):
#     # Temperature of saturated humid air at atmospheric pressure
#     return 164.630366 + 1.832295 * 10 ** (-3) * p_v + 4.27215 * 10 ** (-10) * p_v ** 2 + 3.738954 * 10 ** 3 * p_v ** (-1) - 7.01204 * 10 ** 5 * p_v ** (-2) + 16.161488 * math.log(p_v) - 1.437169 * 10 ** (-4) * p_v * math.log(p_v)

# """
# CHECK SATURATION LEVEL
# """
# def checkSaturation(i_ma_act, x_act):

#     T_db = getDB(i_ma_act, x_act)
#     T_wb = getWB(x_act)

#     if T_wb > T_db:
#         return True
#     else:
#         return False

# """
# CALCULATE THE DIFFERENT STREAMS IN A SPECIFIC COOLING TOWER
# """

# def coolingTower(Me, T_w_n, T_a_n, m_w_n, m_a_n, w_n, H, p_abs=101712.27, r_0 = 2501598):

#     T_w_n = T_w_n + 273.15
#     T_a_n = T_a_n + 273.15
#     m_w_n = m_w_n
#     m_a_n = m_a_n
#     w_n = w_n
#     c_pa_act = get_c_pa((T_w_n + 273.15)/2)
#     c_pv_act = get_c_pv((T_w_n + 273.15)/2)
    
#     waterTemp = []
#     airTemp = []
#     Humidity = []
#     waterFlow = []
#     Enthalpy = []
#     BAAZ = []

#     waterTemp.append(T_w_n)
#     airTemp.append(T_a_n)
#     Humidity.append(w_n)
#     waterFlow.append(m_w_n)    
#     Enthalpy.append(get_i_ma(c_pv_act, c_pa_act, T_a_n, w_n))

#     step = 12
#     baaz_total = 0.06734183400000007
#     deltaBaaz = baaz_total/step
#     baaz = 0
#     BAAZ.append(baaz)
#     SAT = False

#     for i in range(step):   

#         T_w_n = waterTemp[-1]
#         T_a_n = airTemp[-1]
#         w_n = Humidity[-1]
#         m_w_n = waterFlow[-1]
#         i_a_n = Enthalpy[-1]
#         baaz += BAAZ[-1] + deltaBaaz
#         BAAZ.append(baaz)

#         WT = RK4("waterTemp", T_w_n)
#         AT = RK4("airTemperature", T_a_n)
#         HU = RK4("Humidity", w_n)
#         WF = RK4("waterFlow", m_w_n)
#         EN = RK4("Enthalpy", i_a_n)


#         for j in range(4):
#             if SAT == False:
                
#                 T_mid = (T_w_n + 273.15)/2
#                 c_pv = get_c_pv(T_mid)
#                 c_pa = get_c_pa(T_mid)
#                 c_pw = get_c_pw(T_mid)
#                 p_vwb = get_p_wv(getWB(w_n))
#                 p_wv = get_p_wv(T_w_n)
#                 w_sw = get_w_ws(p_abs, p_vwb)
#                 Le = get_Le(w_sw, w_n)
#                 w_sw = get_w_ws(p_abs, p_wv)
#                 dmw_dZ = get_dmw_dz(baaz, w_sw, w_n)
#                 WF.param.append(dmw_dZ)

#                 dX_dZ = get_dX_dz(baaz, w_sw, w_n, m_a_n)
#                 HU.param.append(dX_dZ)

#                 dTa_dZ = get_dTa_dz(baaz, Le, T_w_n, T_a_n, c_pa, c_pv, w_n, w_sw, m_a_n)
#                 AT.param.append(dTa_dZ)

#                 dTw_dZ = get_dTw_dz(baaz, Le, T_w_n, T_a_n, c_pa, c_pv, r_0, c_pw, w_sw, w_n, m_w_n)
#                 WT.param.append(dTw_dZ)

#                 dha_dZ = get_dha_dz(c_pa, w_n, c_pv, dTa_dZ, T_a_n, dX_dZ)
#                 EN.param.append(dha_dZ)

#             else:
#                 dmw_dZ = get_dmw_dz_sat()
#                 dX_dZ = get_dX_dZ_sat()
#                 dTa_dZ = get_dTa_dZ_sat()
#                 dTw_dZ = get_dTw_dZ_sat()

#             if j == 2:
#                 baaz = BAAZ[-1] + deltaBaaz
#                 T_w_n = WT.value + dTw_dZ
#                 T_a_n = AT.value + dTa_dZ
#                 w_n = HU.value + dX_dZ
#                 m_w_n = WF.value + dX_dZ
#                 i_a_n = EN.value + dha_dZ

#             else:
#                 baaz = BAAZ[-1] + deltaBaaz
#                 T_w_n = WT.value + dTw_dZ/2
#                 T_a_n = AT.value + dTa_dZ/2
#                 w_n = HU.value + dX_dZ/2
#                 m_w_n = WF.value + dX_dZ/2
#                 i_a_n = EN.value + dha_dZ/2

#         waterTemp.append(WT.getNewValue())
#         airTemp.append(AT.getNewValue())
#         Humidity.append(HU.getNewValue())
#         waterFlow.append(WF.getNewValue())

#         # if SAT == False:
#         #         if checkSaturation(Enthalpy[-1], Humidity[-1]):
#         #             SAT = True

#     print("sth")

# """
# CALCULATE THE MERKEL NUMBER FOR GIVEN COOLING TOWER PARAMETERS
# """
# def Merkel(T_wi_U, T_wo_U, T_a_in, w_U, m_wi_U, m_a_U, p_abs=101712.27):
    
#     T_wi = T_wi_U + 273.15
#     T_wo = T_wo_U + 273.15
#     w = w_U
#     i_ma = get_i_ma(get_c_pv(T_wo), get_c_pa(T_a_in + 273.15), T_a_in + 273.15, w)
#     p_abs = 101712.27
#     n = 100
#     m_wi = m_wi_U
#     m_a = m_a_U

#     Humidity = []
#     Enthalpy = []
#     Merkel = []
#     Temperature = []
#     waterFlow = []

#     Humidity.append(w)
#     Enthalpy.append(i_ma)
#     Merkel.append(0)
#     Temperature.append(T_wo)

#     SAT = False

#     delta_T_w = round((T_wi - T_wo)/n, 4)
#     for i in range(n):
                
#         w_n = Humidity[-1]
#         i_ma_n = Enthalpy[-1]
#         Me_n = Merkel[-1]
#         T_w_n  = Temperature[-1]

#         # Humidity ratio of air
#         J = RK4("j", w_n)
#         # Enthalpy of air
#         K = RK4("k", i_ma_n)
#         # Merkel constant of the cooling tower
#         L = RK4("k", Me_n)

#         T_w_0 = T_w_n
#         for itr in range(4):

#             if SAT == False:
#                 T_mid = (T_w_n + 273.15)/2
#                 c_pa = get_c_pa(T_mid)
#                 c_pv = get_c_pv(T_mid)
#                 c_pw = get_c_pw(T_mid)
#                 p_wv = get_p_wv(T_w_n)
#                 w_ws = get_w_ws(p_abs, p_wv)
#                 i_fgw = get_i_fgw(273.15)
#                 i_v = get_i_v(i_fgw, c_pv, T_w_n)
#                 i_masw = get_i_masw(c_pa, T_w_n , w_ws, i_v)
#                 Le = get_Le(w_ws, w_n)
#                 mw_ma = get_mv_ma(m_wi, m_a, w_n)
#                 waterFlow.append((m_wi-((mw_ma * m_a_U)) * 3600)/1000)
#                 # waterFlow.append(mw_ma * m_a)
#                 j = get_j(delta_T_w, c_pw, mw_ma, w_ws, w_n, i_masw, i_ma_n, Le, i_v, T_w_n)
#                 # j = round(j,6)
#                 J.param.append(j)
#                 k = get_k(delta_T_w, c_pw, mw_ma, w_ws, w_n, T_w_n-273.15, i_masw, i_ma_n, Le, i_v)
#                 # k = round(k,2)
#                 K.param.append(k)
#                 l = get_l(delta_T_w, c_pw, i_masw, Le, w_ws, i_v, w_n, T_w_n-273.15, i_ma_n)
#                 # l = round(l,5)
#                 L.param.append(l)
#             else:
#                 T_wb = getWB(Humidity[-1])
#                 T_db = getDB(Enthalpy[-1], Humidity[-1])
#                 T_wb= (T_wb + T_db)/2
#                 p_vwb = get_p_wv(T_wb)
#                 w_sa = get_w(T_wb, get_satT(p_vwb), p_vwb, p_abs)
#                 T_mid = (T_w_n + 273.15)/2
#                 c_pa = get_c_pa(T_mid)
#                 c_pv = get_c_pv(T_mid)
#                 c_pw = get_c_pw(T_mid)
#                 p_wv = get_p_wv(T_w_n)
#                 w_ws = get_w_ws(p_abs, p_wv)
#                 i_fgw = get_i_fgw(273.15)
#                 i_v = get_i_v(i_fgw, c_pv, T_w_n)
#                 i_masw = get_i_masw(c_pa, T_w_n , w_ws, i_v)
#                 Le = get_Le(w_ws, w_n)
#                 mw_ma = get_mv_ma(m_wi, m_a, w_n)
#                 waterFlow.append((m_wi-((mw_ma * m_a_U)) * 3600)/1000)
#                 # waterFlow.append(mw_ma * m_a)
#                 j = get_j(delta_T_w, c_pw, mw_ma, w_ws, w_sa, i_masw, i_ma_n, Le, i_v, T_w_n)
#                 # j = round(j,6)
#                 J.param.append(j)
#                 k = get_k(delta_T_w, c_pw, mw_ma, w_ws, w_sa, T_w_n-273.15, i_masw, i_ma_n, Le, i_v)
#                 # k = round(k,2)
#                 K.param.append(k)
#                 l = get_l(delta_T_w, c_pw, i_masw, Le, w_ws, i_v, w_sa, T_w_n-273.15, i_ma_n)
#                 # l = round(l,5)
#                 L.param.append(l)

#             if i == 2:
#                 i_ma_n = K.value + k 
#                 w_n = J.value + j    
#                 T_w_n = T_w_0 + delta_T_w
#             else:
#                 i_ma_n = K.value + k/2 
#                 w_n = J.value + j/2 
#                 T_w_n = T_w_0 + delta_T_w/2
        
#         Humidity.append((J.getNewValue()))
#         Enthalpy.append((K.getNewValue()))
#         Merkel.append((L.getNewValue()))
#         Temperature.append(Temperature[-1] + delta_T_w)

#         if SAT == False:
#             if checkSaturation(Enthalpy[-1], Humidity[-1]):
#                 SAT = True

#     return Merkel[-1]

# # Validation
# merkelNum = Merkel(37, 23, 30, 0.00262, 3, 3)
# Kloppers = Merkel(39.67, 27.77, 9.7, 0.00616336, 3.999, 4.134)

# coolingTower(merkelNum, 23, 30, 2.93, 3, 0.00262, 1.2)

Me = 1.8613
H = 1.2
m_w = 3


n = 1
while True:
    BAAZ = []
    HEIGHT = [] 
    deltaMe = Me / n
    deltaH = H / n
    A = 0
    actMe = 0
    actH = 0
    for i in range(n):
        nextMe = actMe + deltaMe
        nextH = actH + deltaH
        if i == 0:
            A = (nextMe * nextH)/2
            baaz = A * m_w
            BAAZ.append(baaz)
            HEIGHT.append((actH + nextH)/2)
            actMe = nextMe
            actH = nextH
        else:
            A = (actMe + nextMe)/2 * (nextH - actH)
            baaz = A * m_w
            BAAZ.append(baaz)
            HEIGHT.append((actH + nextH)/2)
            actMe = nextMe
            actH = nextH
    if n == 100:
        break
    else:
        n += 1

baaz = BAAZ[-1] + (BAAZ[-1] - BAAZ[-2])
print()