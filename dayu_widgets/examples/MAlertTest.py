#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.MAlert import MAlert
from dayu_widgets.MButtonGroup import MPushButtonGroup
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *


class MAlertTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MAlertTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addWidget(MAlert(text='Normal Message', type=MAlert.InfoType, parent=self))
        main_lay.addWidget(MAlert(text='Success Message', type=MAlert.SuccessType, parent=self))
        main_lay.addWidget(MAlert(text='Warning Message', type=MAlert.WarningType, parent=self))
        main_lay.addWidget(MAlert(text='Error Message', type=MAlert.ErrorType, parent=self))
        main_lay.addWidget(MLabel(u'不同的提示信息类型'))
        main_lay.addWidget(MDivider('closable'))
        main_lay.addWidget(MAlert(text='Error Message', type=MAlert.ErrorType, closable=True, parent=self))
        main_lay.addWidget(MDivider('data bind'))
        self.register_field('msg', '')
        self.register_field('msg_type', MAlert.InfoType)
        alert = MAlert(closable=True, parent=self)

        self.bind('msg', alert, 'text')
        self.bind('msg_type', alert, 'type')
        button_grp = MPushButtonGroup()
        button_grp.set_button_list([
            {'text': 'error',
             'clicked': functools.partial(self.slot_change_alert, 'password is wrong', MAlert.ErrorType)},
            {'text': 'success',
             'clicked': functools.partial(self.slot_change_alert, 'login success', MAlert.SuccessType)},
            {'text': 'no more error', 'clicked': functools.partial(self.slot_change_alert, '', MAlert.InfoType)}
        ])
        main_lay.addWidget(alert)
        main_lay.addWidget(button_grp)
        main_lay.addStretch()

    def slot_change_alert(self, alert_text, alert_type):
        self.set_field('msg_type', alert_type)
        self.set_field('msg', alert_text)


if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme
    app = QApplication(sys.argv)
    test = MAlertTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
