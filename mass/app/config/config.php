<?php
$CONFIG = array (
  'instanceid' => 'ocpg820ubcpn',
  'passwordsalt' => 'MtrycOZv+XmMq8+Z/6CHYzIl6CYN8y',
  'secret' => 'G+AZDeHIs5ytOhd3+w2w0Cj9k3ykgEQTeJL/xv2kPQ7tgQg7',
  'trusted_domains' => 
  array (
    0 => 'localhost',
    1 => 'nextcloud.fabianvolkers.com',
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'mysql',
  'version' => '18.0.0.10',
  'overwrite.cli.url' => 'http://nextcloud.fabianvolkers.com',
  'dbname' => 'nextcloud_db',
  'dbhost' => 'db',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'nextcloud',
  'dbpassword' => 'sV7CbxGCtNkZWhC9PLlExJ04',
  'installed' => true,

  /**
  * When generating URLs, Nextcloud attempts to detect whether the server is
  * accessed via ``https`` or ``http``. However, if Nextcloud is behind a proxy
  * and the proxy handles the ``https`` calls, Nextcloud would not know that
  * ``ssl`` is in use, which would result in incorrect URLs being generated.
  * Valid values are ``http`` and ``https``.
  */
  'overwriteprotocol' => 'https',
);
