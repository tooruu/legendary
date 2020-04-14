#!/usr/bin/env python
# coding: utf-8


class GameAsset:
    def __init__(self):
        self.app_name = ''
        self.asset_id = ''
        self.build_version = ''
        self.catalog_item_id = ''
        self.label_name = ''
        self.namespace = ''
        self.metadata = dict()

    @classmethod
    def from_egs_json(cls, json):
        tmp = cls()
        tmp.app_name = json.get('appName', '')
        tmp.asset_id = json.get('assetId', '')
        tmp.build_version = json.get('buildVersion', '')
        tmp.catalog_item_id = json.get('catalogItemId', '')
        tmp.label_name = json.get('labelName', '')
        tmp.namespace = json.get('namespace', '')
        tmp.metadata = json.get('metadata', {})
        return tmp

    @classmethod
    def from_json(cls, json):
        tmp = cls()
        tmp.app_name = json.get('app_name', '')
        tmp.asset_id = json.get('asset_id', '')
        tmp.build_version = json.get('build_version', '')
        tmp.catalog_item_id = json.get('catalog_item_id', '')
        tmp.label_name = json.get('label_name', '')
        tmp.namespace = json.get('namespace', '')
        tmp.metadata = json.get('metadata', {})
        return tmp


class Game:
    def __init__(self, app_name='', app_title='', asset_info=None, app_version='', metadata=None):
        self.metadata = dict() if metadata is None else metadata  # store metadata from EGS
        self.asset_info = asset_info if asset_info else GameAsset()  # asset info from EGS

        self.app_version = app_version
        self.app_name = app_name
        self.app_title = app_title
        self.base_urls = []  # base urls for download, only really used when cached manifest is current

    @classmethod
    def from_json(cls, json):
        tmp = cls()
        tmp.metadata = json.get('metadata', dict())
        tmp.asset_info = GameAsset.from_json(json.get('asset_info', dict()))
        tmp.app_name = json.get('app_name', 'undefined')
        tmp.app_title = json.get('app_title', 'undefined')
        tmp.app_version = json.get('app_version', 'undefined')
        tmp.base_urls = json.get('base_urls', list())
        return tmp

    @property
    def __dict__(self):
        """This is just here so asset_info gets turned into a dict as well"""
        return dict(metadata=self.metadata, asset_info=self.asset_info.__dict__,
                    app_name=self.app_name, app_title=self.app_title,
                    app_version=self.app_version, base_urls=self.base_urls)


class InstalledGame:
    def __init__(self, app_name='', title='', version='', manifest_path='', base_urls=None,
                 install_path='', executable='', launch_parameters='', prereq_info=None):
        self.app_name = app_name
        self.title = title
        self.version = version

        self.manifest_path = manifest_path
        self.base_urls = list() if not base_urls else base_urls
        self.install_path = install_path
        self.executable = executable
        self.launch_parameters = launch_parameters
        self.prereq_info = prereq_info

    @classmethod
    def from_json(cls, json):
        tmp = cls()
        tmp.app_name = json.get('app_name', '')
        tmp.version = json.get('version', '')
        tmp.title = json.get('title', '')

        tmp.manifest_path = json.get('manifest_path', '')
        tmp.base_urls = json.get('base_urls', list())
        tmp.install_path = json.get('install_path', '')
        tmp.executable = json.get('executable', '')
        tmp.launch_parameters = json.get('launch_parameters', '')
        tmp.prereq_info = json.get('prereq_info', None)
        return tmp