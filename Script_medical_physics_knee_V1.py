# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# Script copyright (C) Fabilone Santos da Silva
# Contributors: Felix Mass Milian

##### OBSERVAÇÕES E CUIDADOS NA UTILIZAÇÃO DO SCRIPT #####
## Para aplicação de deslocamento o valor informado é 2x o valor real
##### END OBSERVAÇÕES BLOCK #####

import bpy
import os

### Set Model Parameters ###
xDimension = 1
yDimension = 1
eixoX = 0
eixoY = 0
eixoZ = 0
pi = 3.1416 #Pi approximation defined by Blender
### End Parameters ###

xnewDM = 0
ynewDM = 0
grau = 0
locx = 0
locy = 0
locz = 0
eixo = ""
opc = ""
obj = ""
opr = "" 

#==================================================================================#
# Here the options are set                              
#==================================================================================#
#Setting Options:
#ajustes 
#ajustes_objeto
opc = ""

if opc == "ajustes":
	#Reading dimensions
	xnewDM = 0.1
	ynewDM = 0.1 
	xDimension = xDimension - xnewDM 
	yDimension = yDimension - ynewDM 
	#Clearing the scene
	bpy.ops.object.select_all(action='DESELECT')
	
	#Selecting all objects
	bpy.ops.object.select_all(action='TOGGLE')
    #Applying scaling in X
	bpy.ops.transform.resize(value=(xDimension, 1.0, 1.0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	#Applying scaling in Y
	bpy.ops.transform.resize(value=(1.0, yDimension, 1.0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

else:
	if opc == "ajustes_objeto":
		#==================================================================================#
		# Here operations are set
		#==================================================================================#
		#Setting Options:
		#scaling
		#rotation
		#translate
		
		opr = ""
		#Setting Options:
		#femur
		#patela
		#tibia
		
		obj = ""
		#Setting Options:
		#X
		#Y
		#Z
		
		eixo = "X"		
		#Clearing the scene
		bpy.ops.object.select_all(action='DESELECT')
		#Selecting object
		bpy.ops.object.select_pattern(pattern= obj, case_sensitive=False, extend=True)
		
		#Rotation Operation
		if opr == "rotation":
			#Defining new rotation
			grau = 0
			if eixo == "X":
				eixoX = ( grau * pi )/180
				#Applying rotation in X
				bpy.ops.transform.rotate(value=eixoX, axis=(1.0, 0.0, 0.0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
			if eixo == "Y":
				eixoY = ( grau * pi )/180
				#Applying rotation in Y
				bpy.ops.transform.rotate(value=eixoY, axis=(0.0, 1.0, 0.0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
			if eixo == "Z":
				eixoZ = ( grau * pi )/180
				#Applying rotation in Z
				bpy.ops.transform.rotate(value=eixoZ, axis=(0.0, 0.0, 1.0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
		
		#Scaling Operation
		if opr == "scaling":
			#Defining new scaling
			if eixo == "X":
				xnewDM = 1
				xDimension = xDimension - xnewDM 				
				#Applying scalin in X
				bpy.ops.transform.resize(value=(xDimension, 1.0, 1.0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
			if eixo == "Y":
				ynewDM = 1
				yDimension = yDimension - ynewDM 				
				#Applying scalin in Y
				bpy.ops.transform.resize(value=(1.0, yDimension, 1.0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
		
		#Translate Operation
		if opr == "translate":
			#Defining new translate
			if eixo == "X":
				locx = 0				
				#Applying translate in X
				bpy.ops.transform.translate(value=(locx, 0.0, 0.0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=True)
			if eixo == "Y":
				locy = 0
				#Applying translate in Y
				bpy.ops.transform.translate(value=(0.0, locy, 0.0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=True)
			if eixo == "Z":
				locz = 0
				#Applying translate in Z
				bpy.ops.transform.translate(value=(0.0, 0.0, locz), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=True)
				