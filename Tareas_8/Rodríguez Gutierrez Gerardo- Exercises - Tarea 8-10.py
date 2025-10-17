import scipy.signal as signal
# Datos
fs = 1500  
nyq = fs / 2 
# Frecuencias de paso y detención
f_pass = 10  # Hz
f_stop = 20  # Hz
# Normalización
wp = f_pass / nyq  
ws = f_stop / nyq 
# Tolerancias
gpass = 3  
gstop = 30  
# Cálculo del orden para diferentes filtros
N_butter, wn_butter = signal.buttord(wp, ws, gpass, gstop)
N_cheby1, wn_cheby1 = signal.cheb1ord(wp, ws, gpass, gstop)
N_cheby2, wn_cheby2 = signal.cheb2ord(wp, ws, gpass, gstop)
N_ellip, wn_ellip = signal.ellipord(wp, ws, gpass, gstop)
print("Orden del filtro Butterworth:", N_butter)
print("Orden del filtro Chebyshev Tipo I:", N_cheby1)
print("Orden del filtro Chebyshev Tipo II:", N_cheby2)
print("Orden del filtro Elíptico:", N_ellip)
