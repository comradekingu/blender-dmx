import bpy
from bpy.types import Operator, Menu

from src.i18n import DMX_i18n

# # Source > Configure

# class DMX_OP_Patch_Source_Configure(Operator):
#     bl_label = DMX_i18n.OP_PATCH_UNIVERSE_ADD
#     bl_description = DMX_i18n.OP_PATCH_UNIVERSE_ADD_DESC
#     bl_idname = "dmx.patch_source_configure"

#     def execute(self, context):
#         print('[OP: ADD UNIVERSE]')
#         return {'FINISHED'}

# # Universe > Add

# class DMX_OP_Patch_Universe_Add(Operator):
#     bl_label = DMX_i18n.OP_PATCH_UNIVERSE_ADD
#     bl_description = DMX_i18n.OP_PATCH_UNIVERSE_ADD_DESC
#     bl_idname = "dmx.patch_universe_add"

#     def execute(self, context):
#         print('[OP: ADD UNIVERSE]')
#         return {'FINISHED'}

# # Fixture > Add

# class DMX_OP_Patch_Fixture_Add(Operator):
#     bl_label = DMX_i18n.OP_PATCH_FIXTURE_ADD
#     bl_description = DMX_i18n.OP_PATCH_FIXTURE_ADD_DESC
#     bl_idname = "dmx.patch_fixture_add"

#     def execute(self, context):
#         print('[OP: ADD FIXTURE]')
#         return {'FINISHED'}

# # Fixture > Add Batch

# class DMX_OP_Patch_Fixture_AddBatch(Operator):
#     bl_label = DMX_i18n.OP_PATCH_FIXTURE_ADDBATCH
#     bl_description = DMX_i18n.OP_PATCH_FIXTURE_ADDBATCH_DESC
#     bl_idname = "dmx.patch_fixture_addbatch"

#     def execute(self, context):
#         print('[OP: ADD FIXTURE BATCH]')
#         return {'FINISHED'}

# # Fixture > Remove

# class DMX_OP_Patch_Fixture_Remove(Operator):
#     bl_label = DMX_i18n.OP_PATCH_FIXTURE_REMOVE
#     bl_description = DMX_i18n.OP_PATCH_FIXTURE_REMOVE_DESC
#     bl_idname = "dmx.patch_fixture_remove"

#     def execute(self, context):
#         print('[OP: REMOVE FIXTURE]')
#         return {'FINISHED'}

# # Build Fixtures

# class DMX_OP_Patch_Build(Operator):
#     bl_label = DMX_i18n.OP_PATCH_BUILD
#     bl_description = DMX_i18n.OP_PATCH_BUILD_DESC
#     bl_idname = "dmx.patch_build"

#     def execute(self, context):
#         print('[OP: BUILD FIXTURES]')
#         return {'FINISHED'}