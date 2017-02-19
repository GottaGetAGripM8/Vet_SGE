# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Client(models.Model): #Un CLIENTE tiene varias MASCOTAS
    _name = 'vet.client'
    name = fields.Char(string="Nombre del cliente", required=True)
    client_id = fields.One2many('vet.pet','pet_id', string="Mascota")

class Pet(models.Model): #Varias MASCOTAS tienen un mismo dueño(CLIENTE)
    _name = 'vet.pet'
    name = fields.Char(string="Nombre de la mascota", required=True)
    pet_id = fields.Many2one('vet.client', string="Cliente")
