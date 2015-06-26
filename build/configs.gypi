# HTML5 runtime
# 
# Copyright (C) 2015 Zhang Ji Peng
# Contact: onecoolx@gmail.com

{
  'configurations': {
    'Debug': {
      'conditions': [
        ['OS=="win"', {
          'defines': [
            '_DEBUG',
          ],
          'msvs_configuration_attributes': {
            'ConfigurationType': '2',
            'CharacterSet': '1',
          },
          'msvs_settings': {
            'VCCLCompilerTool': {
			  'Optimization': '0',
			  'MinimalRebuild': 'true',
			  'ExceptionHandling': '0',
			  'BasicRuntimeChecks': '3',
			  'RuntimeLibrary': '1',
			  'TreatWChar_tAsBuiltInType': 'false',
			  'RuntimeTypeInfo': 'false',
			  'WarningLevel': '3',
			  'WarnAsError': 'true',
			  'SuppressStartupBanner': 'true',
			  'DebugInformationFormat': '3'
            },
            'VCLinkerTool': {
				'LinkIncremental': '1',
				'SuppressStartupBanner': 'true',
				'GenerateDebugInformation': 'true',
				'RandomizedBaseAddress': '1',
				'DataExecutionPrevention': '0',
				'TargetMachine': '1'
            },
          },
        }],
        ['OS=="linux"', {
          'defines': [
            '_DEBUG',
          ],
          'cflags_cc': [
            '-O0',
            '-Wall',
            '-g',
            '-fPIC',
            '-fno-rtti',
            '-fno-exceptions',
            '-Wno-unused-result',
          ],
        }],
      ],
    },
    'Release': {
      'conditions': [
        ['OS=="win"', {
          'defines': [
            'NDEBUG',
          ],
          'msvs_configuration_attributes': {
            'ConfigurationType': '2',
            'CharacterSet': '1',
          },
          'msvs_settings': {
            'VCCLCompilerTool': {
			  'Optimization': '3',
			  'InlineFunctionExpansion': '2',
			  'FavorSizeOrSpeed': '1',
			  'WholeProgramOptimization': 'true',
			  'StringPooling': 'true',
			  'ExceptionHandling': '0',
			  'RuntimeLibrary': '0',
			  'EnableFunctionLevelLinking': 'true',
			  'EnableEnhancedInstructionSet': '2',
			  'FloatingPointModel': '2',
			  'TreatWChar_tAsBuiltInType': 'false',
			  'RuntimeTypeInfo': 'false',
			  'WarningLevel': '3',
			  'WarnAsError': 'true',
			  'SuppressStartupBanner': 'true',
			  'DebugInformationFormat': '3'
            },
            'VCLinkerTool': {
				'LinkIncremental': '1',
				'SuppressStartupBanner': 'true',
				'GenerateDebugInformation': 'false',
				'GenerateMapFile': 'true',
				'LinkTimeCodeGeneration': '1',
				'RandomizedBaseAddress': '1',
				'DataExecutionPrevention': '0',
				'TargetMachine': '1'
            },
          },
        }],
        ['OS=="linux"', {
          'defines': [
            'NDEBUG',
          ],
          'cflags_cc': [
            '-O2',
            '-Wall',
            '-fPIC',
            '-fno-rtti',
            '-fno-exceptions',
            '-Wno-unused-result',
          ],
        }],
      ],
    },
  },
}