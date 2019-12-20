import Vorpal from "vorpal"
import shell from "shelljs"
import fs from "fs"
import path from "path"
import glob from "glob"
import chalk from "chalk"
import { S3 } from "aws-sdk"
import { AWSAPI } from "../utils/aws/apis"

export function s3(vorpal: Vorpal) {
	new Command(vorpal)
}

class Command {
	constructor(private vorpal: Vorpal) {
		vorpal
			.command("s3 convert")
			.option("--bulk", "Bulk Process")
			.option("--dest <dest>", "Destination URI/KeyPath")
			.option("--from <from>", "From Extension")
			.option("--to <to>", "To Extension")
			.action((args) => this.converter(args))
		vorpal
			.command("s3 remove")
			.action((args) => this.remover())
	}

	async converter(args: Vorpal.Args) {
		shell.echo(chalk.red("[!] 확장자 변환 및 업로드 시작"))
		if (args.options.bulk) {
			const result = await AWSAPI.listObjects(args.options.dest)
			for (const objs of result) {


				await this.bulkConvert(objs!, args.options.from, args.options.to)
			}
		}
		else {
			const key = await this.urlParse(args.options.dest)
			await this.processConverter(key!, args.options.from, args.options.to)
		}
		shell.echo(chalk.green("[!] 확장자 변환 및 업로드 완료!"))
	}

	async bulkConvert(objs: S3.Object[], from: string, to: string) {
		const names = []
		for (const obj of objs) {
			if (!obj.Key) continue
			names.push(obj.Key)
		}
		for (const keyName of names) {
			if (keyName!.indexOf(from) != -1) {
				await this.processConverter(keyName!, from, to)
			}
			else {
				continue
			}
		}
	}

	async processConverter(key: string, from: string, to: string) {
		const obj = await AWSAPI.getObject(key)
		this.downloadFile(key, obj.Body!)
		this.changeExtension(key, from, to)
		await this.uploadFile(key, from, to)
		console.log(chalk.yellow(`[+] 확장자 변환 및 업로드 - ${key}`))
	}

	async urlParse(dest: string) {
		const baseURI = "https://zigbang.s3-ap-northeast-1.amazonaws.com/"
		if (dest.indexOf(baseURI) != -1) {
			const keyPath = decodeURI(dest).split(baseURI)[1]
			return keyPath
		}
	}

	downloadFile(key: string, buffer: Object) {
		const keyPath = path.dirname(key)
		if (!fs.existsSync(keyPath)) {
			shell.mkdir('-p', keyPath)
		}
		fs.writeFileSync(`./${key}`, buffer)
	}

	changeExtension(key: string, from: string, to: string) {
		const originPath = path.resolve(key)
		const destPath = path.resolve(originPath).replace(from, "")
		shell.exec(`convert "${originPath}" "${destPath}${to}"`)
	}

	async uploadFile(key: string, from: string, to: string) {
		const originPath = key.replace(from, "")
		const result = glob.sync(`${originPath}*${to}`)

		for (const destination of result) {
			const fileBuf = Buffer.from(`./${destination}`)
			await AWSAPI.putObject(destination, fileBuf)
		}
	}

	async remover() {
		shell.exec("rm -r ./users")
	}
}
