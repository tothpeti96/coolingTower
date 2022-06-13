def get_cp_m(T, m_a, m_w):
    x = m_w/m_a
    return 1.006 * T + 1.86 * x * T + 2501

def get_alpha_LA(K, cp_m):
    return K * cp_m

def get_K(m_w, m_a, A):
    return 2 * ((m_w / A)**0.45) * ((m_a/A)**0.6)

def get_W_sat(p_ws_sat, p_a):
    return 0.622 * (p_ws_sat / (p_a - p_ws_sat))

def get_W_a(T):
    return 4 * 10**(-7) * T ** 3 + 3 * 10**(-6) * T ** 2 + 3 * 10 ** (-4) * T + 0.0037  

def get_dW_dZ(L, K, m_a, W_sat, W_a):
    return ((L * K)/ m_a) * (W_sat - W_a)

def get_cp_w(T):
    return 8 * 10**(-5) * T ** 4 - 0.014 * T ** 3 + 1.0055 * T ** 2 - 32.99 * T + 42199

# Saturation pressure of moist air
def get_p_sat(T):
    return 0.0006 * T ** 4 + 0.0214 * T ** 3 + 0.8053 * T ** 2 + 52.157 * T + 750.38

def get_dTa(alfa_LA, L, m_a, cp_sat, dW_dZ, T_w, T_a, cp_m):
    return (((alfa_LA * L)/m_a) + (cp_sat * dW_dZ)) * ((T_w - T_a)/cp_m)

def get_dTw(m_a, m_w, cp_w, dTa_dZ, cp_m, dW_dZ, T_w, cp_steamSat, T_a, H_w):
    return  - (m_a)/(m_w * cp_w) * (dTa_dZ * cp_m + dW_dZ * (cp_w * T_w + cp_steamSat * T_a + H_w))

def get_dW(L, K, m_a, W_sat, W_a):
    return (L * K / m_a) * (W_sat - W_a)

def d_mv(m_a, dW_dZ):
    return m_a * (dW_dZ)

def get_H_w(T):
    return -2.4337 * T + 2502.2

def Runge_Kutta(L0,L1,n):

    m_w = 0.754                                     
    m_a = 1.158                                     
    A = 3.76
    L = L1

    Tw_out = 31.22
    Ta_in = 37.05
    p_a = 101325

    # Calculating step size
    h = (L1-L0)/n
   
    dW_dZ_0 = get_dW(L, get_K(m_w, m_a, A), m_a, get_W_sat(get_p_sat(Tw_out), p_a), get_W_a(Ta_in))
    dTa_dZ_0 = get_dTa(get_alpha_LA(get_K(m_w, m_a, A), get_cp_m(Tw_out, m_a, m_w)), L, m_a, 2676, dW_dZ_0, Tw_out, Ta_in, get_cp_m(Tw_out, m_a, m_w))
 
    for i in range(n):
        # dW_dZ_k1 = h * get_dW(L, K, m_a, get_W_sat(get_p_sat(Tw_out), p_a), get_W_a(Ta_in))
        # dW_dZ_k2 = h * get_dW((L + h/2), K, m_a, (dW_dZ_0 + dW_dZ_k1/2), get_W_a(Ta_in))
        # dW_dZ_k3 = h * get_dW((L + h/2), K, m_a, (dW_dZ_0 + dW_dZ_k2/2), get_W_a(Ta_in))
        # dW_dZ_k4 = h * get_dW((L + h), K, m_a, (dW_dZ_0 + dW_dZ_k3),get_W_a(Ta_in))
        # dW_dZ = (dW_dZ_k1+2*dW_dZ_k2+2*dW_dZ_k3+dW_dZ_k4)/6

        dW_dZ = get_dW(L, get_K(m_w, m_a, A),  m_a, get_W_sat(get_p_sat(Tw_out), p_a), get_W_a(Ta_in))

        dTa_dZ_k1 = h * get_dTa(get_alpha_LA(get_K(m_w, m_a, A), get_cp_m(Tw_out, m_a, m_w)), L, m_a, 2676, dW_dZ_0, Tw_out, Ta_in, get_cp_m(Tw_out, m_a, m_w))
        dTa_dZ_k2 = h * get_dTa(get_alpha_LA(get_K(m_w, m_a, A), get_cp_m(Tw_out, m_a, m_w)), (L + h/2), m_a, 2676, dW_dZ_0, Tw_out, (Ta_in + dTa_dZ_k1/2), get_cp_m(Tw_out, m_a, m_w))
        dTa_dZ_k3 = h * get_dTa(get_alpha_LA(get_K(m_w, m_a, A), get_cp_m(Tw_out, m_a, m_w)), (L + h/2), m_a, 2676, dW_dZ_0, Tw_out, (Ta_in + dTa_dZ_k2/2), get_cp_m(Tw_out, m_a, m_w))
        dTa_dZ_k4 = h * get_dTa(get_alpha_LA(get_K(m_w, m_a, A), get_cp_m(Tw_out, m_a, m_w)), (L + h/2), m_a, 2676, dW_dZ_0, Tw_out, (Ta_in + dTa_dZ_k3), get_cp_m(Tw_out, m_a, m_w))
        dTa_dZ = (dTa_dZ_k1+2*dTa_dZ_k2+2*dTa_dZ_k3+dTa_dZ_k4)/6
        Ta_in = Ta_in - dTa_dZ

        dTw_dZ_k1 = h *get_dTw(m_a, m_w, get_cp_w(Tw_out), dTa_dZ_0, get_cp_m(Tw_out, m_a, m_w), dW_dZ_0, Tw_out, get_p_sat(Tw_out), Ta_in, get_H_w(Tw_out))
        dTw_dZ_k2 = h *get_dTw(m_a, m_w, get_cp_w(Tw_out + dTw_dZ_k1/2), dTa_dZ_0, get_cp_m((Tw_out + dTw_dZ_k1/2), m_a, m_w), dW_dZ_0, (Tw_out + dTw_dZ_k1/2), get_p_sat((Tw_out + dTw_dZ_k1/2)), Ta_in, get_H_w((Tw_out + dTw_dZ_k1/2)))
        dTw_dZ_k3 = h *get_dTw(m_a, m_w, get_cp_w(Tw_out + dTw_dZ_k2/2), dTa_dZ_0, get_cp_m((Tw_out + dTw_dZ_k2/2), m_a, m_w), dW_dZ_0, (Tw_out + dTw_dZ_k2/2), get_p_sat((Tw_out + dTw_dZ_k2/2)), Ta_in, get_H_w((Tw_out + dTw_dZ_k2/2)))
        dTw_dZ_k4 = h *get_dTw(m_a, m_w, get_cp_w(Tw_out + dTw_dZ_k3/2), dTa_dZ_0, get_cp_m((Tw_out + dTw_dZ_k3/2), m_a, m_w), dW_dZ_0, (Tw_out + dTw_dZ_k3/2), get_p_sat((Tw_out + dTw_dZ_k3/2)), Ta_in, get_H_w((Tw_out + dTw_dZ_k3/2)))
        dTw_dZ = (dTw_dZ_k1+2*dTw_dZ_k2+2*dTw_dZ_k3+dTw_dZ_k4)/6
        Tw_out = Tw_out - dTw_dZ

        dmw_dZ = m_a * dW_dZ_0
        m_w = m_w + dmw_dZ 
        dW_dZ_0 = dW_dZ
        dTa_dZ_0 = dTa_dZ 
        print("{}\t{}\t{}".format(round(L-h, 2), round(Ta_in,2), round(Tw_out,2)))
        L = L - h

Runge_Kutta(0, 1, 15)