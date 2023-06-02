from django.utils.html import format_html
from django import template
register = template.Library()

@register.filter()
def as_table(model_instances):
    header = "<tr>"
    for field in model_instances[0]._meta.fields:
        header += f"<th scope = 'col'>{field.verbose_name}</th>"
    header += "</tr>"

     # Create the table rows with data
    rows = ""
    for instance in model_instances:
        row_class = ""
        status = instance.status

        if status == 'OVER-STOCKED':
            row_class = "table-primary"
        elif status == 'GOOD':
            row_class = "table-success"
        elif status == 'LOW':
            row_class = "table-danger"
        elif status == 'REORDER':
            row_class = "table-warning"
        elif status == 'OUT OF STOCK':
            row_class = "table-dark"

        row = f"<tr class='{row_class}'>"
        for field in instance._meta.fields:
            value = getattr(instance, field.name)
            row += f"<td>{value}</td>"
        row += "</tr>"
        rows += row
        model = instance._meta.model_name
        model = model.upper()
    table = f"<div class='table-responsive'><table class='table table-striped table-hover caption-top table table-bordered'><caption>{model}</caption><thead class='table-dark'>{header}</thead><tbody>{rows}</tbody></table></div>"
    return format_html(table)