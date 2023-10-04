"""Роботы!."""
import json

from datetime import datetime, timedelta
from django.http import FileResponse
from django.views import View
from xlsxwriter.workbook import Workbook
from robots.models import Robot
from R4C.utils import CSRFExemptMixin
from django.http import JsonResponse
from .forms import RobotForm
from django.db.models import Count


class RobotView(CSRFExemptMixin, View):
    def post(self, request):
        """Добавление экземпляра робота."""

        data = json.loads(request.body.decode('utf-8'))
        data['serial'] = data['model'] + '-' + data['version']

        form = RobotForm(data)

        if not form.is_valid():
            return JsonResponse(form.errors)

        form.save()
        return JsonResponse(data)


class RobotReports(CSRFExemptMixin, View):
    def get(self, request):
        """Контроллер - создание отчета за неделю."""

        report = Workbook('report.xlsx')
        bold = report.add_format({'bold': True})

        end_date = datetime.now()
        start_date = end_date - timedelta(weeks=1)

        all_week_robots = Robot.objects.order_by(
            'serial'
        ).values(
            'model', 'version',
        ).filter(
            created__range=(start_date, end_date)
        ).annotate(
            count_serial=Count('serial')
        )

        row, col = 1, 0

        tmp = None

        for robot in all_week_robots:
            if tmp != robot['model']:
                worksheet = report.add_worksheet(name=(robot['model']))
                worksheet.write('A1', 'Модель', bold)
                worksheet.write('B1', 'Версия', bold)
                worksheet.write('C1', 'Количество за неделю', bold)
                tmp = robot['model']
                row = 1
            worksheet.write(row, col, robot['model'])
            worksheet.write(row, col + 1, robot['version'])
            worksheet.write(row, col + 2, robot['count_serial'])
            row += 1

        report.close()

        return FileResponse(open('report.xlsx', 'rb'))
