import bpy
import os
from lib import pygdtf
import json

from bpy.types import PropertyGroup
from bpy.props import ( StringProperty,
                        CollectionProperty,
                        IntProperty )

from src.i18n import DMX_i18n
from src.lang import DMX_Lang
_ = DMX_Lang._


class DMX_Patch_ProfileBreak(PropertyGroup):

    n_channels: IntProperty(
        name = DMX_i18n.PROP_PATCH_PROFILE_NAME,
        description = DMX_i18n.PROP_PATCH_PROFILE_NAME_DESC
    )

class DMX_Patch_ProfileMode(PropertyGroup):

    name: StringProperty(
        name = DMX_i18n.PROP_PATCH_PROFILE_NAME,
        description = DMX_i18n.PROP_PATCH_PROFILE_NAME_DESC
    )

    breaks: CollectionProperty(
        name = DMX_i18n.PROP_PATCH_PROFILE_NAME,
        description = DMX_i18n.PROP_PATCH_PROFILE_NAME_DESC,
        type = DMX_Patch_ProfileBreak
    )


class DMX_Patch_Profile(PropertyGroup):

    name: StringProperty(
        name = DMX_i18n.PROP_PATCH_PROFILE_NAME,
        description = DMX_i18n.PROP_PATCH_PROFILE_NAME_DESC
    )

    short_name: StringProperty(
        name = DMX_i18n.PROP_PATCH_PROFILE_SHORT_NAME,
        description = DMX_i18n.PROP_PATCH_PROFILE_SHORT_NAME_DESC
    )

    filename: StringProperty(
        name = DMX_i18n.PROP_PATCH_PROFILE_NAME,
        description = DMX_i18n.PROP_PATCH_PROFILE_NAME_DESC
    )

    modes: CollectionProperty(
        type = DMX_Patch_ProfileMode
    )

    @staticmethod
    def get_profiles_path() -> str:
        """Return the path to the "profiles" folder."""

        FILE_PATH = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(FILE_PATH,'..','..','..','assets','profiles')

    @staticmethod
    def get_profile_list():
        """List gdtf files in in profiles folder"""

        profiles_path = DMX_Patch_Profile.get_profiles_path()
        profiles = []
        for file in os.listdir(profiles_path):
            file_path = os.path.join(profiles_path, file)
            fixture_type = pygdtf.FixtureType(file_path)
            modes=[]
            for mode in fixture_type.dmx_modes:
                channels=pygdtf.utils.get_dmx_channels(fixture_type, mode.name)
                dmx_breaks = []
                for dmx_break in channels:
                    dmx_breaks.append(len(dmx_break))
                modes.append({"name": mode.name, "breaks":tuple(dmx_breaks)})
            profiles.append({"name": f"{fixture_type.manufacturer} @ {fixture_type.long_name}",
                             "short_name": fixture_type.short_name,
                             "filename": file,
                             "modes":modes})
                    
        return profiles

    @staticmethod
    def load():
        patch = bpy.context.scene.dmx.patch
        patch.profiles.clear()
        profiles = DMX_Patch_Profile.get_profile_list()


        for profile in profiles:
            patch.profiles.add()
            patch.profiles[-1].name = profile['name']
            patch.profiles[-1].short_name = profile['short_name']
            patch.profiles[-1].filename = profile['filename']

            for mode in profile['modes']:
                patch.profiles[-1].modes.add()
                patch.profiles[-1].modes[-1].name = mode['name']
                for n in mode['breaks']:
                    patch.profiles[-1].modes[-1].breaks.add()
                    patch.profiles[-1].modes[-1].breaks[-1].n_channels = n

class DMX_Patch_Import_Gdtf_Profile(PropertyGroup):

    name: StringProperty(
        name = _("Fixture name"),
        description = _("Manufacturer and fixture name")
    )

    rid: IntProperty(
        name = _("Revision ID"),
        description = _("File identifier in the GDTF Share") 
    )


    @staticmethod
    def get_profiles_path() -> str:
        """Return the path to the "profiles" folder."""

        FILE_PATH = os.path.dirname(os.path.abspath(__file__))
        #return os.path.join(FILE_PATH,'..','..','..','assets','profiles')
        return FILE_PATH

    @staticmethod
    def get_profile_list():
        """List gdtf files in in profiles folder"""
        profiles_path = DMX_Patch_Import_Gdtf_Profile.get_profiles_path()
        with open(os.path.join(profiles_path, "start.json")) as f:
            data = json.load(f)
        return data

    @staticmethod
    def load():
        print("loading start")
        patch = bpy.context.scene.dmx.patch
        patch.share_profiles.clear()
        profiles = DMX_Patch_Import_Gdtf_Profile.get_profile_list()


        for profile in profiles:
            patch.share_profiles.add()
            name = f"{profile['manufacturer']} @ {profile['fixture']}"
            patch.share_profiles[-1].name = name
            patch.share_profiles[-1].rid = profile['rid']
        print("loading done")

