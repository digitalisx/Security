rule Malware_pattern
{
	strings:
		$string = "300 USD"
		$hex = { 33 30 30 20 55 53 44 }

	condition:
		$string or $hex
}
