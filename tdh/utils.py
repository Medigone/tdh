import frappe

@frappe.whitelist(allow_guest=True)
def submit_contact_form():
    try:
        # Créer un nouveau document Formulaire Contact
        contact = frappe.get_doc({
            'doctype': 'Formulaire Contact',
            'prenom': frappe.form_dict.get('first-name'),
            'nom': frappe.form_dict.get('last-name'),
            'email': frappe.form_dict.get('email'),
            'telephone': frappe.form_dict.get('phone'),
            'message': frappe.form_dict.get('message')
        })
        
        contact.insert(ignore_permissions=True)
        
        frappe.response['message'] = 'Message envoyé avec succès'
        return {'status': 'success'}

    except Exception as e:
        frappe.log_error(f'Erreur formulaire de contact: {str(e)}')
        frappe.response['message'] = 'Une erreur est survenue lors de l\'envoi du message'
        return {'status': 'error'}