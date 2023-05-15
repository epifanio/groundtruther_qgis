""" docstring """
import yaml
from pydantic.error_wrappers import ValidationError
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from starlette.templating import Jinja2Templates
from groundtruther.pygui.app_settings_gui import AppSettings
from config_model import HabcamSettings
from groundtruther.config.config import config
import os
from pathlib import Path

# root_dir = os.environ.get("HBC_ROOT_DIR")
root_dir = os.path.dirname(__file__)

class ConfigDialog(QDialog, AppSettings):
    """docstring"""

    def __init__(self, parent=None):
        super().__init__()
        QDialog.__init__(self, parent)

        self.setupUi(self)
        self.broadcast_port.setValidator(
            QRegExpValidator(QRegExp("^[0-9]{12}$")))
        # toot_dir from environment var
        self.root_dir = os.path.dirname(__file__) # os.environ.get("HBC_ROOT_DIR")
        self.config = config # os.environ.get('HBC_CONFIG')
        self.gpu_avaibility_value = False
        self.templates_path = Path.joinpath(
            Path(self.root_dir), 'config/templates')
        self.templates = Jinja2Templates(directory=self.templates_path)

        self.select_image_path.clicked.connect(self.set_image_path)
        self.select_metadata_path.clicked.connect(self.set_metadata_path)
        self.select_imageannotation_path.clicked.connect(
            self.set_imageannotation_path)
        self.select_mbes_path.clicked.connect(self.set_mbes_path)
        self.select_vrt_path.clicked.connect(self.set_vrt_path)
        self.select_kml_path.clicked.connect(self.set_kml_path)

        self.gpu_avaibility.currentIndexChanged.connect(
            self.set_gpu_avaibility)

        self.setOption.clicked.connect(self.write_config)
        self.quit.clicked.connect(self.close)
        self.settings_value = self.get_settings()
        print("self.settings_value", self.settings_value)
        if self.settings_value:
            self.filemanager.setText(
                self.settings_value["Filesystem"]["filemanager"])
            self.image_path.setText(self.settings_value["HabCam"]["imagepath"])
            self.metadata_path.setText(
                self.settings_value["HabCam"]["imagemetadata"])
            self.imageannotation_path.setText(
                self.settings_value["HabCam"]["imageannotation"]
            )
            self.mbes_path.setText(self.settings_value["Mbes"]["soundings"])
            self.kml_path.setText(self.settings_value["Export"]["kmldir"])
            self.vrt_path.setText(self.settings_value["Export"]["vrtdir"])
            self.broadcast_ip.setText(self.settings_value["Broadcast"]["ip"])
            self.broadcast_port.setText(
                str(self.settings_value["Broadcast"]["port"]))
            # self.mapviewer_basemap.setText(
            #     self.settings_value["Mapviewer"]["basemap"])
        else:
            widget_container = {
                "Filesystem": {"filemanager": self.filemanager},
                "HabCam": {
                    "imagepath": self.image_path,
                    "imagemetadata": self.metadata_path,
                    "imageannotation": self.imageannotation_path,
                },
                "Mbes": {"soundings": self.mbes_path},
                "Export": {"kmldir": self.kml_path, "vrtdir": self.vrt_path},
                "Broadcast": {"ip": self.broadcast_ip, "port": self.broadcast_port},
                # "Mapviewer": {"basemap": self.mapviewer_basemap},
                "Processing": {"GPU": False, "GRASS_API": "http://localhost/docs"},
            }

            self.settings = self.get_settings2()
            self.filemanager.setText(
                self.settings["Filesystem"]["filemanager"])
            self.image_path.setText(self.settings["HabCam"]["imagepath"])
            self.metadata_path.setText(
                self.settings["HabCam"]["imagemetadata"])
            self.mbes_path.setText(self.settings["Mbes"]["soundings"])
            self.kml_path.setText(self.settings["Export"]["kmldir"])
            self.vrt_path.setText(self.settings["Export"]["vrtdir"])
            self.broadcast_ip.setText(self.settings["Broadcast"]["ip"])
            self.broadcast_port.setText(
                str(self.settings["Broadcast"]["port"]))
            # self.mapviewer_basemap.setText(
            #     self.settings["Mapviewer"]["basemap"])
            if self.settings["Processing"]["GPU"]:
                self.gpu_avaibility.setCurrentText('Enabled')
            else:
                self.gpu_avaibility.setCurrentText('Disabled')
            self.grass_api_endpoint.setText(
                self.settings["Processing"]["GRASS_API"])

            bad_keys = self.validate_config(get_bad_keys=True)
            bad_key = [str(list(i.keys())[0]) for i in bad_keys]
            bad_values = [i[list(i.keys())[0]] for i in bad_keys]
            print(bad_key, bad_values)
            for i in bad_values:
                print("bad value for: ", i)
            for i in bad_keys:
                widget_container[str(list(i.keys())[0])][
                    str(i[list(i.keys())[0]])
                ].setText("")
        # if os.environ['RAPIDSAI'] == 'enabled':
        #     pass
        # else:
        #     self.gpu_avaibility.setEnabled(False)
        self.gpu_avaibility.setEnabled(False)
        self.broadcast_config_box.setVisible(False)
        self.broadcast_config_box.hide()
        self.vrt_label.hide()
        self.vrt_path.hide()
        self.select_vrt_path.hide()

    def get_settings2(self):
        """docstring"""
        try:
            with open(self.config, "r", encoding="utf8") as config:
                settings = yaml.safe_load(config)
                return settings
        except FileNotFoundError as notfound:
            return False

    def get_settings(self):
        """docstring"""
        try:
            with open(self.config, "r", encoding="utf8") as config:
                settings = yaml.safe_load(config)
                if validate_config2(settings):
                    return settings
                else:
                    return False
        except FileNotFoundError as notfound:
            error_message(str(notfound))
            # show_dialog()
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Set Config file",
                self.metadata_path.text(),
                "All Files (*);;Text Files (*.yaml)",
                options=options,
            )
            if file_name:
                self.settings = self.get_settings2()
            return self.settings

    def validate_config(self, get_bad_keys=False):
        """docstring"""
        try:
            m = HabcamSettings(
                Mbes={"soundings": self.settings["Mbes"]["soundings"]},
                HabCam={
                    "imagepath": self.settings["HabCam"]["imagepath"],
                    "imagemetadata": self.settings["HabCam"]["imagemetadata"],
                },
                Export={
                    "kmldir": self.settings["Export"]["kmldir"],
                    "vrtdir": self.settings["Export"]["vrtdir"],
                },
                Broadcast={
                    "ip": self.settings["Broadcast"]["ip"],
                    "port": int(self.settings["Broadcast"]["port"]),
                },
                # Mapviewer={"basemap": self.settings["Mapviewer"]["basemap"]},
                Filesystem={
                    "filemanager": self.settings["Filesystem"]["filemanager"]},
                Processing={
                    "gpu_avaibility": self.settings["Processing"]["GPU"],
                    "grass_api_endpoint": self.settings["Processing"]["GRASS_API"],
                }
            )
            return True
        except ValidationError as msg:
            bad_keys = []
            # error_msg = "The following Parameters have invalid values: \n"
            for i in msg.errors():
                # print(i)
                # error_msg = error_msg+f"""{i['loc'][0]} : {i['loc'][1]} \n"""
                bad_keys.append({i["loc"][0]: i["loc"][1]})
            # error_message(error_msg)
            if get_bad_keys:
                return bad_keys
            else:
                return False

    def write_config(self):
        """docstring"""
        try:
            int(self.broadcast_port.text())
        except ValueError:
            error_message(
                "Invalid PORT number setting to default value \n 7000")
            self.broadcast_port.setText("7000")
        gui_settings = self.get_gui_settings()
        if validate_config2(gui_settings):
            # if self.validate_config():
            # check if the template exist first
            hbc_config = self.templates.get_template("config_template.yaml").render(
                {
                    "filemanager": self.filemanager.text(),
                    "imagepath": self.image_path.text(),
                    "imagemetadata": self.metadata_path.text(),
                    "imageannotation": self.imageannotation_path.text(),
                    "soundings": self.mbes_path.text(),
                    "kmldir": self.kml_path.text(),
                    "vrtdir": self.vrt_path.text(),
                    "ip": self.broadcast_ip.text(),
                    "port": self.broadcast_port.text(),
                    "gpu_avaibility": self.gpu_avaibility_value,
                    "grass_api_endpoint": self.grass_api_endpoint.text(),
                }
            )
            # config = Path.joinpath(Path(self.root_dir), 'config/config.yaml')
            
            with open(self.config, "w+", encoding="utf8") as yaml_file:
                yaml_file.write(hbc_config)
                print(f"wrote new config: \n {hbc_config}")

    def set_gpu_avaibility(self, index):
        if self.gpu_avaibility.itemText(index) == 'Enabled':
            self.gpu_avaibility_value = True
        else:
            self.gpu_avaibility_value = False

    def set_metadata_path(self):
        """docstring"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Set HabCam Image Metadata",
            self.metadata_path.text(),
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )
        if file_name:
            self.metadata_path.setText(file_name)

    def set_imageannotation_path(self):
        """docstring"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Set HabCam Image Metadata",
            self.imageannotation_path.text(),
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )
        if file_name:
            self.imageannotation_path.setText(file_name)

    def set_image_path(self):
        """docstring"""
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(
            self, "Set HabCam Image directory", self.image_path.text(), options=options
        )
        if directory:
            self.image_path.setText(directory)

    def set_kml_path(self):
        """docstring"""
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(
            self, "Set KML export directory", self.kml_path.text(), options=options
        )
        if directory:
            self.kml_path.setText(directory)

    def set_vrt_path(self):
        """docstring"""
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(
            self, "Set VRT export directory", self.vrt_path.text(), options=options
        )
        if directory:
            self.vrt_path.setText(directory)

    def set_mbes_path(self):
        """docstring"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Set MBES datasource",
            self.metadata_path.text(),
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )
        if file_name:
            self.mbes_path.setText(file_name)

    def get_gui_settings(self):
        """docstring"""
        gui_settings = {
            "Mbes": {"soundings": self.mbes_path.text()},
            "HabCam": {
                "imagepath": self.image_path.text(),
                "imagemetadata": self.metadata_path.text(),
                "imageannotation": self.imageannotation_path.text(),
            },
            "Export": {"kmldir": self.kml_path.text(), "vrtdir": self.vrt_path.text()},
            "Broadcast": {
                "ip": self.broadcast_ip.text(),
                "port": int(self.broadcast_port.text()),
            },
            # "Mapviewer": {"basemap": self.mapviewer_basemap.text()},
            "Filesystem": {"filemanager": self.filemanager.text()},
        }
        return gui_settings


def show_dialog():
    """docstring"""
    # dialog = QDialogClass()
    dialog = ConfigDialog()
    dialog.exec_()


def validate_config2(settings, get_bad_keys=False):
    """docstring"""
    try:
        m = HabcamSettings(
            Mbes={"soundings": settings["Mbes"]["soundings"]},
            HabCam={
                "imagepath": settings["HabCam"]["imagepath"],
                "imagemetadata": settings["HabCam"]["imagemetadata"],
                "imageannotation": settings["HabCam"]["imageannotation"],
            },
            Export={
                "kmldir": settings["Export"]["kmldir"],
                "vrtdir": settings["Export"]["vrtdir"],
            },
            Broadcast={
                "ip": settings["Broadcast"]["ip"],
                "port": int(settings["Broadcast"]["port"]),
            },
            # Mapviewer={"basemap": settings["Mapviewer"]["basemap"]},
            Filesystem={"filemanager": settings["Filesystem"]["filemanager"]},
        )
        return True
    except ValidationError as msg:
        bad_keys = []
        error_msg = "The following Parameters have invalid values: \n"
        for i in msg.errors():
            print(i)
            error_msg = error_msg + f"""{i['loc'][0]} : {i['loc'][1]} \n"""
            bad_keys.append({i["loc"][0]: i["loc"][0]})
        error_message(error_msg)
        if get_bad_keys:
            return bad_keys
        else:
            return False


def get_settings2(config):
    """docstring"""
    try:
        with open(config, "r", encoding="utf8") as config_file:
            settings = yaml.safe_load(config_file)
            return settings
    except FileNotFoundError as notfound:
        return False


def get_settings(config):
    """docstring"""
    try:
        with open(config, "r", encoding="utf8") as config_file:
            settings = yaml.safe_load(config_file)
            if validate_config2(settings):
                return settings
            else:
                return False
    except FileNotFoundError as notfound:
        error_message(str(notfound))
        # show_dialog()
        return False


def error_message(message):
    """docstring"""
    alert = QMessageBox()
    alert.setText(message)
    alert.exec()
