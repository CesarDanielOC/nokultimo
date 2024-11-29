from django.shortcuts import render, redirect
from .models import Paciente  # Cambiar de Reseña a Paciente
from datetime import datetime

def inicio_vistaPaciente(request):
    los_pacientes = Paciente.objects.all()  # Cambiado de reseña a paciente
    return render(request, 'gestionarPaciente.html', {'mispacientes': los_pacientes})

def registrarPaciente(request):
    if request.method == 'POST':
        id_paciente = request.POST["numidpaciente"]
        id_producto = request.POST["numidproducto"]
        id_cliente = request.POST["numidcliente"]
        calificacion = request.POST["numcalificacion"]
        comentario = request.POST["txtcomentario"]
        
        # Convertir fecha de reseña al formato adecuado
        fecha_paciente_str = request.POST["txtfechareseña"]
        fecha_paciente = datetime.strptime(fecha_paciente_str, '%Y-%m-%d').date()  # Convertir la cadena a fecha
        
        estado = request.POST["txtestado"]

        guardar_paciente = Paciente.objects.create(
            id_paciente=id_paciente, 
            id_producto=id_producto,
            id_cliente=id_cliente, 
            calificacion=calificacion,
            comentario=comentario, 
            fecha_reseña=fecha_paciente,  # Guardamos la fecha correctamente formateada
            estado=estado
        )
        return redirect('Paciente')
    return render(request, 'gestionarPaciente.html')

def seleccionarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    return render(request, "editarPaciente.html", {"mispacientes": paciente})

def editarPaciente(request):
    if request.method == 'POST':
        id_paciente = request.POST["numidpaciente"]
        id_producto = request.POST["numidproducto"]
        id_cliente = request.POST["numidcliente"]
        calificacion = request.POST["numcalificacion"]
        comentario = request.POST["txtcomentario"]
        
        # Convertir fecha de reseña al formato adecuado
        fecha_paciente_str = request.POST["txtfechareseña"]
        fecha_paciente = datetime.strptime(fecha_paciente_str, '%Y-%m-%d').date()  # Convertir la cadena a fecha
        
        estado = request.POST["txtestado"]

        paciente = Paciente.objects.get(id_paciente=id_paciente)

        paciente.id_producto = id_producto
        paciente.id_cliente = id_cliente
        paciente.calificacion = calificacion
        paciente.comentario = comentario
        paciente.fecha_reseña = fecha_paciente  # Guardamos la fecha correctamente formateada
        paciente.estado = estado
        paciente.save()

        return redirect('Paciente')

def borrarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    paciente.delete()

    return redirect('Paciente')
