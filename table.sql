CREATE TABLE IF NOT EXISTS `speedtest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `download` float NOT NULL DEFAULT '0',
  `upload` float NOT NULL DEFAULT '0',
  `ping` float NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
