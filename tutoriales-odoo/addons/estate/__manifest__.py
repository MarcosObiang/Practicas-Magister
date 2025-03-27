{
    "name": "Estate Module",
    "version": "0.2",
    "author": "yo",
    "summary": "Módulo para la gestión de bienes raíces",
    "description": """
        Este módulo permite gestionar información de bienes raíces.
    """,
    "category": "Real Estate",
    "installable": True,
    "application": True,
    "auto_install": False,
    "data": [
        "security/ir.model.access.csv",
        "views/estate/estate_fields_list.xml",
        "views/estate/estate_form_fields.xml",
        "views/estate/estate_search_field.xml",
        "views/estate/estate_property_views.xml",
        "views/property_type/settings_property_view.xml",
        "views/property_type/porperty_types_list.xml",
        "views/property_tag/property_tag_field_list.xml",
        "views/property_tag/property_tag_main_action.xml",
        "views/property_offer/tree_view.xml",
        "views/property_offer/form_view.xml",
        "views/root_menu.xml",
    ],
}
