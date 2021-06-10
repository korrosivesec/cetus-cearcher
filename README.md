# `Cetus Cearcher`

Unofficial CLI tool to query the Cetus API maintained by SparkIT Solutions.

## Installation

Clone the repo and use [Typer CLI](https://typer.tiangolo.com/typer-cli/) to run

or

`pip install cetus-cearcher`


Once installed, you'll need to create a file named `config.py` in the `cetus` directory and declare two variables:

|Variable |Value|
|---|---|
|api_url|API server including protocol ( i.e. `https://example.com` )|
|api_key|API key obtained from the portal|

## Usage

```console
$ cetus [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `example`: Show example result data
* `search`: Search Cetus

## `cetus example`

Show example result data

**Usage**:

```console
$ cetus example [OPTIONS] INDEX:[dns|certstream]
```

**Arguments**:

* `INDEX:[dns|certstream]`: [required]

**Options**:

* `--raw`: Print raw output instead of pretty printed  [default: False]
* `--help`: Show this message and exit.

## `cetus search`

Search Cetus

**Usage**:

```console
$ cetus search [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `certstream`: Search the Cetus Certstream index
* `dns`: Search the Cetus DNS index

### `cetus search certstream`

Search the Cetus Certstream index

**Usage**:

```console
$ cetus search certstream [OPTIONS] QUERY
```

**Arguments**:

* `QUERY`: Lucene formatted query.  [required]

**Options**:

* `--start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: Beginning of search range. Required.  [required]
* `--end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: End of search range. If omitted, end == now  [default: 2021-06-10T17:11:20]
* `--raw`: Print raw output instead of pretty printed  [default: False]
* `--metadata`: Include metadata in output  [default: False]
* `--help`: Show this message and exit.

### `cetus search dns`

Search the Cetus DNS index

**Usage**:

```console
$ cetus search dns [OPTIONS] QUERY
```

**Arguments**:

* `QUERY`: Lucene formatted query.  [required]

**Options**:

* `--start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: Beginning of search range. Required.  [required]
* `--end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: End of search range. If omitted, end == now  [default: 2021-06-10T17:11:20]
* `--raw`: Print raw output instead of pretty printed  [default: False]
* `--metadata`: Include metadata in output  [default: False]
* `--help`: Show this message and exit.
