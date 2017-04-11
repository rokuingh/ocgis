import numpy as np

from ocgis.util.enum import Enum, IntEnum

UNINITIALIZED = -999
OCGIS_BOUNDS = 'bounds'

#: Default netCDF4 output file type
NETCDF_DEFAULT_DATA_MODEL = 'NETCDF4'

#: Default temporal calendar.
DEFAULT_TEMPORAL_CALENDAR = 'standard'

#: Default temporal units.
DEFAULT_TEMPORAL_UNITS = 'days since 0001-01-01 00:00:00'

#: Default name for the time dimension.
DEFAULT_TEMPORAL_NAME = 'time'

#: Default name for coordinate systems in netCDF file if none is provided.
DEFAULT_COORDINATE_SYSTEM_NAME = 'ocgis_coordinate_system'

#: Default sample size variable standard name.
DEFAULT_SAMPLE_SIZE_STANDARD_NAME = 'sample_size'

#: Default sample size variable long name.
DEFAULT_SAMPLE_SIZE_LONG_NAME = 'Statistical Sample Size'

#: Default row coordinate name.
DEFAULT_NAME_ROW_COORDINATES = 'yc'

#: Default column coordinate name.
DEFAULT_NAME_COL_COORDINATES = 'xc'

#: Default corners dimension name.
DEFAULT_NAME_CORNERS_DIMENSION = 'corners'

#: Default rotated pole ellipse for transformation.
PROJ4_ROTATED_POLE_ELLPS = 'sphere'


class HeaderName(object):
    ID_SELECTION_GEOMETRY = 'UGID'
    ID_GEOMETRY = 'GID'

    REALIZATION = 'RLZ'

    VARIABLE = 'VARIABLE'

    TEMPORAL = 'TIME'
    TEMPORAL_BOUNDS = ['LB_TIME', 'UB_TIME']
    TEMPORAL_YEAR = 'YEAR'
    TEMPORAL_MONTH = 'MONTH'
    TEMPORAL_DAY = 'DAY'

    LEVEL = 'LEVEL'
    LEVEL_BOUNDS = ['LB_LEVEL', 'UB_LEVEL']

    VALUE = 'VALUE'

    CALCULATION_KEY = 'CALC_KEY'
    CALCULATION_SOURCE_VARIABLE = 'SRC_VAR'

    DATASET_IDENTIFER = 'DID'


#: Standard name for the unique identifier in GIS files.
OCGIS_UNIQUE_GEOMETRY_IDENTIFIER = HeaderName.ID_SELECTION_GEOMETRY.upper()


class OutputFormatName(object):
    CSV = 'csv'
    CSV_SHAPEFILE = 'csv-shp'
    ESMPY_GRID = 'esmpy'
    GEOJSON = 'geojson'
    METADATA_JSON = 'meta-json'
    METADATA_OCGIS = 'meta-ocgis'
    NETCDF = 'nc'
    SHAPEFILE = 'shp'
    OCGIS = 'ocgis'


#: These output formats are considered vector output formats affected by operations manipulation vector GIS data. For
#: example, vector GIS outputs are always wrapped to -180 to 180 if there is a spherical coordinate system.
VECTOR_OUTPUT_FORMATS = [OutputFormatName.GEOJSON, OutputFormatName.SHAPEFILE, OutputFormatName.CSV_SHAPEFILE]

# Download URL for test datasets.
TEST_DATA_DOWNLOAD_PREFIX = None

#: The day value to use for month centroids.
CALC_MONTH_CENTROID = 16
#: The month value to use for year centroids.
CALC_YEAR_CENTROID_MONTH = 7
#: The default day value for year centroids.
CALC_YEAR_CENTROID_DAY = 1

#: The number of values to use when calculating data resolution.
RESOLUTION_LIMIT = 100

#: The data type to use for NumPy integers.
DEFAULT_NP_INT = np.int
#: The data type to use for NumPy floats.
DEFAULT_NP_FLOAT = np.float

#: Function key prefix for the `icclim` indices library.
ICCLIM_PREFIX_FUNCTION_KEY = 'icclim'

#: NumPy functions enabled for functions evaluated from string representations.
ENABLED_NUMPY_UFUNCS = ('exp', 'log', 'abs', 'power')

#: The value for the 180th meridian to use when wrapping.
MERIDIAN_180TH = 180.
# MERIDIAN_180TH = 179.9999999999999

# The standard key used to identify geometries in a dictionary.
DEFAULT_GEOMETRY_KEY = 'geom'

# The default string width for Fiona output.
FIONA_STRING_LENGTH = 50

# Attributes to remove when a value is changed if they are present in the attributes dictionary. These attributes are
# tuned to specific value ranges and will not apply when a value is changed.
NETCDF_ATTRIBUTES_TO_REMOVE_ON_VALUE_CHANGE = ('scale_value', 'add_offset', 'actual_range', 'valid_range')

NAME_DIMENSION_REALIZATION = 'rlz'
NAME_DIMENSION_TEMPORAL = 'time'
NAME_DIMENSION_LEVEL = 'level'

NAME_BOUNDS_DIMENSION_LOWER = 'lb'
NAME_BOUNDS_DIMENSION_UPPER = 'ub'

NAME_UID_DIMENSION_REALIZATION = 'rid'
NAME_UID_DIMENSION_TEMPORAL = 'tid'
NAME_UID_DIMENSION_LEVEL = 'lid'
NAME_UID_FIELD = 'fid'

# calculation dictionary key defaults
CALC_KEY_KEYWORDS = 'kwds'
CALC_KEY_CLASS_REFERENCE = 'ref'

# Default unique identifier start value.
DEFAULT_UID_START = 1


class DataType(object):
    DIMENSION_SRC_INDEX = np.int32


class AttributeName(object):
    UNIQUE_GEOMETRY_IDENTIFIER = 'ocgis_geom_uid'
    ORIGINAL_SPATIAL_BOUNDS = '_ocgis_original_bounds_name'


class DimensionName(object):
    UNIONED_GEOMETRY = 'ocgis_geom_union'
    GEOMETRY_DIMENSION = 'ocgis_geom'
    TEMPORAL = 'time'


class MiscName(object):
    DEFAULT_FIELD_NAME = 'ocgis_field'


class VariableName(object):
    SPATIAL_MASK = 'ocgis_spatial_mask'
    GEOMETRY_POINT = 'ocgis_point'
    GEOMETRY_POLYGON = 'ocgis_polygon'


# Enumerations for wrapped states and actions. #########################################################################

class WrappedState(IntEnum):
    # Data is wrapped -180 to 180.
    WRAPPED = 1
    # Data is unwrapped 0 to 360.
    UNWRAPPED = 2
    # The wrapped state is unknown due to coordinate values only in the range 0 to 180.
    UNKNOWN = 3


class WrapAction(IntEnum):
    # Wrap the data to -180 to 180.
    WRAP = 1
    # Unwrap the data 0 to 360.
    UNWRAP = 2


########################################################################################################################


# Dimension map key names.
class DimensionMapKey(object):
    GROUPS = 'groups'
    X = 'x'
    Y = 'y'
    Z = 'z'
    TIME = 'time'
    REALIZATION = 'realization'
    CRS = 'crs'
    BOUNDS = 'bounds'
    VARIABLE = 'variable'
    NAMES = 'names'
    LEVEL = 'level'
    GEOM = 'geom'


# MPI Writing flags.
class MPIWriteMode(Enum):
    NORMAL = 0
    TEMPLATE = 1
    FILL = 2
    WRITE = 0
    APPEND = 2


class TagName(object):
    DATA_VARIABLES = '_ocgis_data_variables'


class KeywordArgument(object):
    ADD_BOUNDS = 'add_bounds'
    ADD_GEOM_UID = 'add_geom_uid'
    ALLOW_MASKED = 'allow_masked'
    BOUNDS_NAMES = 'bounds_names'
    CASCADE = 'cascade'
    COMM = 'comm'
    CREATE = 'create'
    CRS = 'crs'
    DATASET = 'dataset'
    DIMENSION_MAP = 'dimension_map'
    DIMENSIONS = 'dimensions'
    DIR_OUTPUT = 'dir_output'
    DRIVER = 'driver'
    EAGER = 'eager'
    EXCLUDE = 'exclude'
    FIELD_NAME = 'field_name'
    FILE_ONLY = 'file_only'
    FOLLOWERS = 'followers'
    FORMAT_TIME = 'format_time'
    GEOM = 'geom'
    GRID = 'grid'
    GRID_ABSTRACTION = 'grid_abstraction'
    HEADER_MAP = 'header_map'
    INIT_VALUE = 'init_value'
    INPLACE = 'inplace'
    INTERSECTS_CHECK = 'intersects_check'
    IS_DATA = 'is_data'
    IS_EMPTY = 'is_empty'
    ITER_KWARGS = 'iter_kwargs'
    KEEP_TOUCHES = 'keep_touches'
    MASK = 'mask'
    MELTED = 'melted'
    OPTIMIZED_BBOX_SUBSET = 'optimized_bbox_subset'
    ORIGINAL_MASK = 'original_mask'
    OUTPUT_FORMAT = 'output_format'
    PARENT = 'parent'
    PATH = 'path'
    PREFIX = 'prefix'
    PRIMARY_MASK = 'primary_mask'
    REPEATERS = 'repeaters'
    RANKS_TO_WRITE = 'ranks_to_write'
    REGRID_DESTINATION = 'regrid_destination'
    REGRID_SOURCE = 'regrid_source'
    RENAME_VARIABLE = 'rename_variable'
    RETURN_SLICE = 'return_slice'
    SNIPPET = 'snippet'
    STANDARDIZE = 'standardize'
    STRICT = 'strict'
    TAG = 'tag'
    UGID = 'ugid'
    UNLIMITED_TO_FIXED_SIZE = 'unlimited_to_fixedsize'
    UNION = 'union'
    UPDATE = 'update'
    URI = 'uri'
    USE_BOUNDS = 'use_bounds'
    VALUE = 'value'
    VARIABLE = 'variable'
    VARIABLE_KWARGS = 'variable_kwargs'
    WITH_PROJ4 = 'with_proj4'
    # WRAPPED_BBOX = 'wrapped_bbox'
    WRITE_MODE = 'write_mode'
    YIELD_BASE = 'yield_base'

    class Defaults(object):
        IS_DATA = False
        STANDARDIZE = True


class DriverKey(object):
    BASE = 'base'
    CSV = 'csv'
    NETCDF = 'netcdf'
    NETCDF_CF = 'netcdf-cf'
    VECTOR = 'vector'


class MPITag(IntEnum):
    BARRIER = 0
    SCATTER = 1
    BCAST = 2
    GATHER = 3


class CFName(object):
    TIME = ('time',)
    X = ['x', 'xc', 'longitude', 'lon']
    Y = ['y', 'yc', 'latitude', 'lat']
    Z = ['z', 'zc', 'level', 'lvl', 'height']
    UNITS = 'units'
    STANDARD_NAME = 'standard_name'
    GRID_MAPPING = 'grid_mapping'

    @classmethod
    def get_name_mapping(cls):
        return {'T': cls.TIME, 'X': cls.X, 'Y': cls.Y, 'Z': cls.Z}


class SubcommName(Enum):
    FIELD_GET = '__ocgis_field_get__'
    FIELD_SUBSET = '__ocgis_field_subset__'
    UGEOM_WRITE = '__ocgis_ugeom_write__'
    NONSPATIAL_SUBSET = '__ocgis_nonspatial_subset__'
    SPATIAL_AVERAGE = '__ocgis_spatial_average__'


class BackTransform(Enum):
    ROTATED_POLE = 'rotated pole'


MPI_COMM_NULL_VALUE = 8675309
