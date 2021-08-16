import numpy_financial as npf

from datetime import datetime
from dateutil.relativedelta import relativedelta
def Calculo(tabla):
    capital=tabla[0]
    capital-=tabla[1]
    plazo=tabla[2]
    interes=0
    cuota = round(npf.pmt(interes, plazo, -capital, 0), 0)
    datos = []
    saldo = capital
    today =tabla[3]
    fecha_dt = datetime.strptime(today, '%Y-%m-%d')

    for i in range(1, plazo+1):
        pago_capital = npf.ppmt(interes, i, plazo, -capital, 0)
        pago_int = cuota - pago_capital
        saldo -= pago_capital
        linea = [fecha_dt, format(cuota, '0,.0f'), format(pago_capital, '0,.0f'), format(pago_int, '0,.0f'), format(saldo, '0,.0f')]
        fecha_dt = fecha_dt + relativedelta(months=1)  
        datos.append(linea)
    return datos