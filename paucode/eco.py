def va(i, nper, pago, vf):
    """Valor actual o valor presente. Se utiliza para actualizar el valor final a una tasa i% en nper periodos de tiempo

    Args:
        i (_type_): Tasa de interes en porcentajes
        nper (_type_): numero de periodos para actualizar
        pago (_type_): pagos periodicos
        vf (_type_): Valor final

    Returns:
        _type_: Valor actual o actualización al momento cero
    """
    return vf/(1+i)**nper