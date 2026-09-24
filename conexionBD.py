from supabase import create_client, Client

SUPABASE_URL = "https://sprsppzkawfxkzjlxmrg.supabase.co" 
SUPABASE_KEY = "sb_publishable_IOYIdsjMVuTjS0Hgn5EKng_m6FAlNmu"

def obtenerClienteSupabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def guardarEvaluacionNube(calidadComida, calidadServicio, porcentajePropina, nivelPropina):
    try:
        clienteSupabase = obtenerClienteSupabase()
        datosEvaluacion = {
            "calidad_comida": calidadComida,
            "calidad_servicio": calidadServicio,
            "porcentaje_propina": porcentajePropina,
            "nivel_propina": nivelPropina
        }
        respuestaPeticion = clienteSupabase.table("registros_propinas").insert(datosEvaluacion).execute()
        return True, respuestaPeticion
    except Exception as errorConexion:
        return False, str(errorConexion)
def obtenerHistorialNube():
    try:
        clienteSupabase = obtenerClienteSupabase()
        respuestaPeticion = clienteSupabase.table("registros_propinas").select("*").order("fecha", desc=True).limit(10).execute()
        return respuestaPeticion.data
    except Exception:
        return []
                     
        