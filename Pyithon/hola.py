#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
datos={
    {
    "SRV001": {
        "WebServer": [45, 32],
        "Database": [65],
        "BackupService": [98, 100, 96]
    },
    "SRV002": {
        "WebServer": [55, 60],
        "ApplicationServer": [75],
        "MonitoringTool": [89, 90]
    },
    "SRV003": {
        "FileStorage": [40, 42, 38],
        "LoggingService": [92]
    },
    "SRV004": {
        "MailServer": [50],
        "WebServer": [60, 65, 58],
    },
    "SRV005": {
        "Database": [70, 75],
        "BackupService": [100]
    }
}
    
    
    }
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))